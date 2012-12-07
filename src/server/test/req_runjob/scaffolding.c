#include "license_pbs.h" /* See here for the software license */
#include <stdlib.h>
#include <stdio.h> /* fprintf */
#include <pthread.h>


#include "attribute.h" /* attribute_def, batch_op */
#include "resource.h" /* resource_def */
#include "server.h" /* server */
#include "pbs_ifl.h" /* PBS_MAXHOSTNAME */
#include "array.h" /* job_array */
#include "pbs_job.h" /* job */
#include "net_connect.h" /* pbs_net_t */
#include "batch_request.h" /* batch_request */
#include "node_func.h" /* node_info */
#include "pbs_nodes.h" /* pbsnode */
#include "work_task.h" /* work_task, work_type */
#include "list_link.h" /* list_link  */
#include "queue.h"

pthread_mutex_t *scheduler_sock_jobct_mutex;
const char *PJobSubState[10];
int svr_tsnodes = 0;
int svr_resc_size = 0;
attribute_def job_attr_def[10];
char *msg_jobrun = "Job Run";
resource_def *svr_resc_def;
char mom_host[PBS_MAXHOSTNAME + 1];
int scheduler_jobct = 0;
struct server server;
int scheduler_sock = -1;
pbs_net_t pbs_mom_addr;
int LOGLEVEL = 0;
char *msg_manager = "%s at request of %s@%s";
int svr_totnodes = 0;



job_array *get_jobs_array(job **pjob)
  {
  fprintf(stderr, "The call to get_jobs_array to be mocked!!\n");
  exit(1);
  }

void account_record(int acctype, job *pjob, char *text)
  {
  fprintf(stderr, "The call to account_record to be mocked!!\n");
  exit(1);
  }

char *parse_servername(char *name, unsigned int *service)
  {
  fprintf(stderr, "The call to parse_servername to be mocked!!\n");
  exit(1);
  }

int job_save(job *pjob, int updatetype, int mom_port)
  {
  fprintf(stderr, "The call to job_save to be mocked!!\n");
  exit(1);
  }

void svr_mailowner(job *pjob, int mailpoint, int force, char *text)
  {
  fprintf(stderr, "The call to svr_mailowner to be mocked!!\n");
  exit(1);
  }

char *find_ts_node(void)
  {
  fprintf(stderr, "The call to find_ts_node to be mocked!!\n");
  exit(1);
  }

void stat_mom_job(char *job_id)
  {
  fprintf(stderr, "The call to stat_mom_job to be mocked!!\n");
  exit(1);
  }

pbs_net_t get_hostaddr(int *local_errno, char *hostname)
  {
  fprintf(stderr, "The call to get_hostaddr to be mocked!!\n");
  exit(1);
  }

struct batch_request *cpy_checkpoint(struct batch_request *preq, job *pjob, enum job_atr ati, int direction)
  {
  fprintf(stderr, "The call to cpy_checkpoint to be mocked!!\n");
  exit(1);
  }

void reply_ack(struct batch_request *preq)
  {
  fprintf(stderr, "The call to reply_ack to be mocked!!\n");
  exit(1);
  }

void free_nodes(node_info **ninfo_arr)
  {
  fprintf(stderr, "The call to free_nodes to be mocked!!\n");
  exit(1);
  }

char *PAddrToString(pbs_net_t *Addr)
  {
  fprintf(stderr, "The call to PAddrToString to be mocked!!\n");
  exit(1);
  }

struct pbsnode *find_nodebyname(char *nodename)
  {
  static struct pbsnode pnode;

  if (!strcmp("bob", nodename))
    return(&pnode);
  else
    return(NULL);
  }

struct work_task *set_task(enum work_type type, long event_id, void (*func)(), void *parm, int get_lock)
  {
  fprintf(stderr, "The call to set_task to be mocked!!\n");
  exit(1);
  }

int depend_on_exec(job *pjob)
  {
  fprintf(stderr, "The call to depend_on_exec to be mocked!!\n");
  exit(1);
  }

int unlock_node(struct pbsnode *the_node, const char *id, char *msg, int logging)
  {
  fprintf(stderr, "The call to unlock_node to be mocked!!\n");
  exit(1);
  }

void req_reject(int code, int aux, struct batch_request *preq, char *HostName, char *Msg)
  {
  fprintf(stderr, "The call to req_reject to be mocked!!\n");
  exit(1);
  }

int is_ts_node(char *nodestr)
  {
  fprintf(stderr, "The call to is_ts_node to be mocked!!\n");
  exit(1);
  }

void *get_next(list_link pl, char *file, int line)
  {
  fprintf(stderr, "The call to get_next to be mocked!!\n");
  exit(1);
  }

void stream_eof(int stream, u_long addr, uint16_t port, int ret)
  {
  fprintf(stderr, "The call to stream_eof to be mocked!!\n");
  exit(1);
  }

void poll_job_task(struct work_task *ptask)
  {
  fprintf(stderr, "The call to poll_job_task to be mocked!!\n");
  exit(1);
  }

void set_resc_assigned(job *pjob, enum batch_op op)
  {
  fprintf(stderr, "The call to set_resc_assigned to be mocked!!\n");
  exit(1);
  }

int job_set_wait(pbs_attribute *pattr, void *pjob, int mode)
  {
  fprintf(stderr, "The call to job_set_wait to be mocked!!\n");
  exit(1);
  }

 resource_def *find_resc_def(resource_def *rscdf, char *name, int limit)
  {
  fprintf(stderr, "The call to find_resc_def to be mocked!!\n");
  exit(1);
  }

void update_array_values(job_array *pa, int old_state, enum ArrayEventsEnum event, char *job_id, long job_atr_hold, int job_exit_status)
  {
  fprintf(stderr, "The call to update_array_values to be mocked!!\n");
  exit(1);
  }

void release_req(struct work_task *pwt)
  {
  fprintf(stderr, "The call to release_req to be mocked!!\n");
  exit(1);
  }

 int set_nodes(job *pjob, char *spec, int procs, char **rtnlist, char **rtnportlist, char *FailHost, char *EMsg)
  {
  fprintf(stderr, "The call to set_nodes to be mocked!!\n");
  exit(1);
  }

struct batch_request *cpy_stage(struct batch_request *preq, job *pjob, enum job_atr ati, int direction)
  {
  fprintf(stderr, "The call to cpy_stage to be mocked!!\n");
  exit(1);
  }

void account_jobstr(job *pjob)
  {
  fprintf(stderr, "The call to account_jobstr to be mocked!!\n");
  exit(1);
  }

int svr_setjobstate(job *pjob, int newstate, int newsubstate, int  has_queue_mutex)
  {
  pjob->ji_qs.ji_state    = newstate;
  pjob->ji_qs.ji_substate = newsubstate;

  return(0);
  }

resource *find_resc_entry(pbs_attribute *pattr, resource_def *rscdf)
  {
  fprintf(stderr, "The call to find_resc_entry to be mocked!!\n");
  exit(1);
  }

job *svr_find_job(char *jobid, int get_subjob)
  {
  fprintf(stderr, "The call to find_job to be mocked!!\n");
  exit(1);
  }

void DIS_tcp_settimeout(long timeout)
  {
  fprintf(stderr, "The call to DIS_tcp_settimeout to be mocked!!\n");
  exit(1);
  }

int send_job_work(char *job_id, char *node_name, int type, int *my_err, struct batch_request *preq)
  {
  fprintf(stderr, "The call to send_job_work to be mocked!!\n");
  exit(1);
  }

void svr_evaljobstate(job *pjob, int *newstate, int *newsub, int forceeval)
  {
  fprintf(stderr, "The call to svr_evaljobstate to be mocked!!\n");
  exit(1);
  }

job *chk_job_request(char *jobid, struct batch_request *preq)
  {
  fprintf(stderr, "The call to chk_job_request to be mocked!!\n");
  exit(1);
  }

int insert_task(all_tasks *at, work_task *wt)
  {
  fprintf(stderr, "The call to insert_task to be mocked!!\n");
  exit(1);
  }

char *threadsafe_tokenizer(char **str, char *delims)
  {
  fprintf(stderr, "The call to threadsafe_tokenizer needs to be mocked!!\n");
  exit(1);
  }

int get_svr_attr_l(int index, long *l)
  {
  return(0);
  }

pbs_queue *get_jobs_queue(job **pjob)
  {
  return((*pjob)->ji_qhdr);
  }

void free_br(struct batch_request *b) {}

int get_svr_attr_str(int index, char **str)
  {
  return(0);
  }

int unlock_queue(struct pbs_queue *the_queue, const char *id, char *msg, int logging)
  {
  return(0);
  }

batch_request *get_remove_batch_request(

  char *br_id)

  {
  return(NULL);
  }

int get_batch_request_id(

  batch_request *preq)

  {
  return(0);
  }

int unlock_ji_mutex(job *pjob, const char *id, char *msg, int logging)
  {
  return(0);
  }

int split_job(job *pjob)
  {
  return(0);
  }

int kill_job_on_mom(char *jobid, struct pbsnode *pnode)
  {
  return(0);
  }

int lock_ji_mutex(job *pjob, const char *id, char *msg, int logging)
  {
  return(0);
  }

batch_request *duplicate_request(struct batch_request *preq)
  {
  return(NULL);
  }

int unlock_ai_mutex(job_array *pa, const char *id, char *msg, int logging)
  {
  return(0);
  }

int enqueue_threadpool_request(void *(*func)(void *), void *arg)

  {
  return(0);
  }
