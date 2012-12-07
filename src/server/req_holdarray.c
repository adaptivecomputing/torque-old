#include <pbs_config.h>   /* the master config generated by configure */
#include <pthread.h>

#include <stdio.h>
#include "libpbs.h"
#include "server_limits.h"
#include "list_link.h"
#include "attribute.h"
#include "server.h"
#include "credential.h"
#include "batch_request.h"
#include "pbs_job.h"
#include "pbs_error.h"
#include "log.h"
#include "../lib/Liblog/log_event.h"
#include "acct.h"
#include "svrfunc.h"
#include "array.h"
#include "csv.h"
#include "ji_mutex.h"

extern int chk_hold_priv(long val, int perm);
extern int get_hold(tlist_head *, char **, pbs_attribute *);
extern int svr_authorize_req(struct batch_request *preq, char *owner,
                               char *submit_host);

extern char *msg_permlog;
extern int LOGLEVEL;


void hold_job(

  pbs_attribute *temphold, /* I */
  void          *j)        /* I */

  {
  long *hold_val;
  long old_hold;

  int newstate;
  int newsub;

  pbs_attribute *pattr;
  job *pjob = (job *)j;

  if (pjob == NULL)
    return;

  hold_val = &pjob->ji_wattr[JOB_ATR_hold].at_val.at_long;
  old_hold = *hold_val;
  *hold_val |= temphold->at_val.at_long;
  pjob->ji_wattr[JOB_ATR_hold].at_flags |= ATR_VFLAG_SET;
  
  pattr = &pjob->ji_wattr[JOB_ATR_checkpoint];
  
  if ((pjob->ji_qs.ji_state == JOB_STATE_RUNNING) &&
      ((pattr->at_flags & ATR_VFLAG_SET) &&
       ((csv_find_string(pattr->at_val.at_str, "s") != NULL) ||
        (csv_find_string(pattr->at_val.at_str, "c") != NULL) ||
        (csv_find_string(pattr->at_val.at_str, "enabled") != NULL))))
    {
    /* TODO */
    /* preq_tmp = alloc_br(preq->rq_type); */
    
    }
  else if (old_hold != *hold_val)
    {
    /* indicate attributes changed  */
    
    pjob->ji_modified = 1;

    svr_evaljobstate(pjob, &newstate, &newsub, 0);

    svr_setjobstate(pjob, newstate, newsub, FALSE);
    }

  } /* END hold_job() */



int req_holdarray(
    
  void *vp) /* I */

  {
  int                   i;
  struct batch_request *preq = (struct batch_request *)vp;
  char                 *pset;
  char                 *range_str;
  int                   rc;
  pbs_attribute         temphold;
  char                  owner[PBS_MAXUSER + 1];
  job_array            *pa;
  job                  *pjob;
  char                  log_buf[LOCAL_LOG_BUF_SIZE];

  pa = get_array(preq->rq_ind.rq_hold.rq_orig.rq_objname);

  if (pa == NULL)
    {
    /* this shouldn't happen since we verify that this is a valid array
       just prior to calling this function */
    req_reject(PBSE_UNKARRAYID, 0, preq, NULL, "unable to find array");
    return(PBSE_NONE);
    }

  get_jobowner(pa->ai_qs.owner, owner);

  if (svr_authorize_req(preq, owner, pa->ai_qs.submit_host) == -1)
    {
    sprintf(log_buf, msg_permlog,
      preq->rq_type, "Array", preq->rq_ind.rq_delete.rq_objname, preq->rq_user, preq->rq_host);

    log_event(PBSEVENT_SECURITY, PBS_EVENTCLASS_JOB, preq->rq_ind.rq_delete.rq_objname, log_buf);

    unlock_ai_mutex(pa, __func__, "1", LOGLEVEL);

    req_reject(PBSE_PERM, 0, preq, NULL, "operation not permitted");
    return(PBSE_NONE);
    }


  if ((rc = get_hold(&preq->rq_ind.rq_hold.rq_orig.rq_attr, &pset,
                     &temphold)) != 0)
    {
    unlock_ai_mutex(pa, __func__, "2", LOGLEVEL);

    req_reject(rc, 0, preq, NULL, NULL);
    return(PBSE_NONE);
    }

  /* if other than HOLD_u is being set, must have privil */

  if ((rc = chk_hold_priv(temphold.at_val.at_long, preq->rq_perm)) != 0)
    {
    unlock_ai_mutex(pa, __func__, "3", LOGLEVEL);

    req_reject(rc, 0, preq, NULL, NULL);
    return(PBSE_NONE);
    }

  /* get the range of jobs to iterate over */
  range_str = preq->rq_extend;
  if ((range_str != NULL) &&
      (strstr(range_str,ARRAY_RANGE) != NULL))
    {
    if ((rc = hold_array_range(pa,range_str,&temphold)) != 0)
      {
      unlock_ai_mutex(pa, __func__, "4", LOGLEVEL);

      req_reject(rc,0,preq,NULL,
        "Error in specified array range");
      return(PBSE_NONE);
      }
    }
  else
    {
    /* do the entire array */
    for (i = 0;i < pa->ai_qs.array_size;i++)
      {
      if (pa->job_ids[i] == NULL)
        continue;

      if ((pjob = svr_find_job(pa->job_ids[i], FALSE)) == NULL)
        {
        free(pa->job_ids[i]);
        pa->job_ids[i] = NULL;
        }
      else
        {
        hold_job(&temphold,pjob);
        unlock_ji_mutex(pjob, __func__, "5", LOGLEVEL);
        }
      }
    }

  unlock_ai_mutex(pa, __func__, "6", LOGLEVEL);

  reply_ack(preq);

  return(PBSE_NONE);
  } /* END req_holdarray() */

