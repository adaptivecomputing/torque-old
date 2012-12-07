#include "license_pbs.h" /* See here for the software license */
#include <stdlib.h>
#include <stdio.h> /* fprintf */

#include "pbs_job.h" /* job_recycler, all_jobs, job */
#include "resizable_array.h"

job_recycler recycler;
int          LOGLEVEL;


int enqueue_threadpool_request(void *(*func)(void *),void *arg)
  {
  fprintf(stderr, "The call to enqueue_threadpool_request to be mocked!!\n");
  exit(1);
  }

int insert_job(struct all_jobs *aj, job *pjob)
  {
  fprintf(stderr, "The call to insert_job to be mocked!!\n");
  exit(1);
  }

job *next_job(struct all_jobs *aj, int *iter)
  {
  fprintf(stderr, "The call to next_job to be mocked!!\n");
  exit(1);
  }

void initialize_all_jobs_array(struct all_jobs *aj)
  {
  fprintf(stderr, "The call to initialize_all_jobs_array to be mocked!!\n");
  exit(1);
  }

int remove_job(struct all_jobs *aj, job *pjob)
  {
  fprintf(stderr, "The call to remove_job to be mocked!!\n");
  exit(1);
  }

void *next_thing(resizable_array *ra, int *iter)
  {
  return(NULL);
  }

int unlock_ji_mutex(job *pjob, const char *id, char *msg, int logging)
  {
  return(0);
  }

int lock_ji_mutex(job *pjob, const char *id, char *msg, int logging)
  {
  return(0);
  }

int lock_alljobs_mutex(struct all_jobs *aj, const char *id, char *msg, int logging)
  {
  return(0);
  }

int unlock_alljobs_mutex(struct all_jobs *aj, const char *id, char *msg, int logging)
  {
  return(0);
  }
