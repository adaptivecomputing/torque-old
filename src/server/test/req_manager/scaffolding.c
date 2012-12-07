#include "license_pbs.h" /* See here for the software license */
#include <stdlib.h>
#include <stdio.h> /* fprintf */

#include "pbs_nodes.h" /* all_nodes, pbsnode, node_check_info, prop */
#include "queue.h" /* all_queues, pbs_queue */
#include "pbs_ifl.h" /* PBS_MAXSERVERNAME */
#include "resource.h" /* resource_def */
#include "attribute.h" /* attribute_def, pbs_attribute, svrattrl */
#include "server.h" /* server */
#include "batch_request.h" /* batch_request */
#include "list_link.h" /* list_link */
#include "work_task.h" /* work_type */

all_nodes allnodes;
int svr_resc_size = 0;
int disable_timeout_check = 1;
all_queues svr_queues;
char *msg_daemonname = "unset";
char *msg_man_del = "deleted";
char *msg_attrtype = "Warning: type of queue %s incompatible with attribute %s";
char *msg_man_cre = "created";
char *msg_man_set = "attributes set: ";
char *msg_manager = "%s at request of %s@%s";
char *msg_man_uns = "attributes unset: ";
char server_name[PBS_MAXSERVERNAME + 1];
resource_def *svr_resc_def;
attribute_def que_attr_def[10];
attribute_def node_attr_def[2];
struct server server;
char *array_disallowed_types[] = {"hi", "hello"};
attribute_def svr_attr_def[10];
int LOGLEVEL = 0;
int svr_chngNodesfile = 0;
int svr_totnodes = 0;


int write_node_note(void)
  {
  fprintf(stderr, "The call to write_node_note to be mocked!!\n");
  exit(1);
  }

pbs_queue *find_queuebyname(char *quename)
  {
  fprintf(stderr, "The call to find_queuebyname to be mocked!!\n");
  exit(1);
  }

void clear_attr(pbs_attribute *pattr, attribute_def *pdef)
  {
  fprintf(stderr, "The call to clear_attr to be mocked!!\n");
  exit(1);
  }

int attr_atomic_node_set(struct svrattrl *plist, pbs_attribute *old, pbs_attribute *new_attr, attribute_def *pdef, int limit, int unkn, int privil, int *badattr)
  {
  fprintf(stderr, "The call to attr_atomic_node_set to be mocked!!\n");
  exit(1);
  }

void reply_ack(struct batch_request *preq)
  {
  fprintf(stderr, "The call to reply_ack to be mocked!!\n");
  exit(1);
  }

void delete_link(struct list_link *old)
  {
  fprintf(stderr, "The call to delete_link to be mocked!!\n");
  exit(1);
  }

void setup_notification(char *pname)
  {
  fprintf(stderr, "The call to setup_notification to be mocked!!\n");
  exit(1);
  }

int chk_characteristic(struct pbsnode *pnode, node_check_info *nci, int *pneed_todo)
  {
  fprintf(stderr, "The call to chk_characteristic to be mocked!!\n");
  exit(1);
  }

struct pbsnode *find_nodebyname(char *nodename)
  {
  fprintf(stderr, "The call to find_nodebyname to be mocked!!\n");
  exit(1);
  }

pbs_queue *que_alloc(char *name, int sv_qs_mutex_held)
  {
  fprintf(stderr, "The call to que_alloc to be mocked!!\n");
  exit(1);
  }

struct work_task *set_task(enum work_type type, long event_id, void (*func)(), void *parm, int get_lock)
  {
  fprintf(stderr, "The call to set_task to be mocked!!\n");
  exit(1);
  }

void effective_node_delete(struct pbsnode *pnode)
  {
  fprintf(stderr, "The call to effective_node_delete to be mocked!!\n");
  exit(1);
  }

int unlock_node(struct pbsnode *the_node, const char *id, char *msg, int logging)
  {
  fprintf(stderr, "The call to unlock_node to be mocked!!\n");
  exit(1);
  }

int find_attr(struct attribute_def *attr_def, char *name, int limit)
  {
  fprintf(stderr, "The call to find_attr to be mocked!!\n");
  exit(1);
  }

void free_prop_list(struct prop *prop)
  {
  fprintf(stderr, "The call to free_prop_list to be mocked!!\n");
  exit(1);
  }

void write_node_state(void)
  {
  fprintf(stderr, "The call to write_node_state to be mocked!!\n");
  exit(1);
  }

struct pbsnode *next_host(all_nodes *an, int *iter, struct pbsnode *held)
  {
  fprintf(stderr, "The call to next_host to be mocked!!\n");
  exit(1);
  }

void req_reject(int code, int aux, struct batch_request *preq, char *HostName, char *Msg)
  {
  fprintf(stderr, "The call to req_reject to be mocked!!\n");
  exit(1);
  }

struct pbsnode *next_node(all_nodes *an, struct pbsnode *current, node_iterator *iter)
  {
  fprintf(stderr, "The call to next_node to be mocked!!\n");
  exit(1);
  }

struct prop *init_prop(char *pname)
  {
  fprintf(stderr, "The call to init_prop to be mocked!!\n");
  exit(1);
  }

int attr_atomic_set(struct svrattrl *plist, pbs_attribute *old, pbs_attribute *new_attr, attribute_def *pdef, int limit, int unkn, int privil, int *badattr)
  {
  fprintf(stderr, "The call to attr_atomic_set to be mocked!!\n");
  exit(1);
  }

void save_characteristic(struct pbsnode *pnode, node_check_info *nci)
  {
  fprintf(stderr, "The call to save_characteristic to be mocked!!\n");
  exit(1);
  }

void *get_next(list_link pl, char *file, int line)
  {
  fprintf(stderr, "The call to get_next to be mocked!!\n");
  exit(1);
  }

void que_free(pbs_queue *pq, int sv_qs_mutex_held)
  {
  fprintf(stderr, "The call to que_free to be mocked!!\n");
  exit(1);
  }

resource_def *find_resc_def(resource_def *rscdf, char *name, int limit)
  {
  fprintf(stderr, "The call to find_resc_def to be mocked!!\n");
  exit(1);
  }

void recompute_ntype_cnts(void)
  {
  fprintf(stderr, "The call to recompute_ntype_cnts to be mocked!!\n");
  exit(1);
  }

int hasprop(struct pbsnode *pnode, struct prop *props)
  {
  fprintf(stderr, "The call to hasprop to be mocked!!\n");
  exit(1);
  }

void attr_atomic_kill(pbs_attribute *temp, attribute_def *pdef, int limit)
  {
  fprintf(stderr, "The call to attr_atomic_kill to be mocked!!\n");
  exit(1);
  }

char *pbse_to_txt(int err)
  {
  fprintf(stderr, "The call to pbse_to_txt to be mocked!!\n");
  exit(1);
  }

pbs_queue *next_queue(all_queues *aq, int *iter)
  {
  fprintf(stderr, "The call to next_queue to be mocked!!\n");
  exit(1);
  }

int init_resc_defs(void)
  {
  fprintf(stderr, "The call to init_resc_defs to be mocked!!\n");
  exit(1);
  }

void free_arst(struct pbs_attribute *attr)
  {
  fprintf(stderr, "The call to free_arst to be mocked!!\n");
  exit(1);
  }

int get_fullhostname(char *shortname, char *namebuf, int bufsize, char *EMsg)
  {
  fprintf(stderr, "The call to get_fullhostname to be mocked!!\n");
  exit(1);
  }

int que_purge(pbs_queue *pque)
  {
  fprintf(stderr, "The call to que_purge to be mocked!!\n");
  exit(1);
  }

int PNodeStateToString(int SBM, char *Buf, int BufSize)
  {
  fprintf(stderr, "The call to PNodeStateToString to be mocked!!\n");
  exit(1);
  }

resource *find_resc_entry(pbs_attribute *pattr, resource_def *rscdf)
  {
  fprintf(stderr, "The call to find_resc_entry to be mocked!!\n");
  exit(1);
  }

int svr_save(struct server *ps, int mode)
  {
  fprintf(stderr, "The call to svr_save to be mocked!!\n");
  exit(1);
  }

int update_nodes_file(struct pbsnode *held)
  {
  fprintf(stderr, "The call to update_nodes_file to be mocked!!\n");
  exit(1);
  }

void list_move(tlist_head *from, tlist_head *to)
  {
  fprintf(stderr, "The call to list_move to be mocked!!\n");
  exit(1);
  }

int unlock_queue(struct pbs_queue *the_queue, const char *method_name, char *msg, int logging)
  {
  fprintf(stderr, "The call to unlock_queue to be mocked!!\n");
  exit(1);
  }

int que_save(pbs_queue *pque)
  {
  fprintf(stderr, "The call to que_save to be mocked!!\n");
  exit(1);
  }

void reinitialize_node_iterator(node_iterator *iter)
  {
  fprintf(stderr, "The call to reinitialize_node_iterator to be mocked!!\n");
  exit(1);
  }

int create_pbs_node(char *objname, svrattrl *plist, int perms, int *bad)
  {
  fprintf(stderr, "The call to create_pbs_node to be mocked!!\n");
  exit(1);
  }

void reply_badattr(int code, int aux, svrattrl *pal, struct batch_request *preq)
  {
  fprintf(stderr, "The call to reply_badattr to be mocked!!\n");
  exit(1);
  }

void reply_text(struct batch_request *preq, int code, char *text)
  {
  fprintf(stderr, "The call to reply_text to be mocked!!\n");
  exit(1);
  }

int safe_strncat(char *str, char *to_append, size_t space_remaining)
  {
  return(0);
  }

int unlock_sv_qs_mutex(pthread_mutex_t *sv_qs_mutex, const char *msg_string)
  {
  return(0);
  }

int lock_sv_qs_mutex(pthread_mutex_t *sv_qs_mutex, const char *msg_string)
  {
  return(0);
  }
