#include "license_pbs.h" /* See here for the software license */
#include <stdlib.h>
#include <stdio.h> /* fprintf */
#include <netdb.h> /* addrinfo */
#include <netinet/in.h>


#include "resizable_array.h" /* resizable_array */
#include "pbs_nodes.h" /* all_nodes, pbsnode */
#include "attribute.h" /* attribute_def, pbs_attribute, svrattrl */
#include "server.h" /* server */
#include "u_tree.h" /* AvlTree */
#include "hash_table.h" /* hash_table_t */
#include "list_link.h" /* list_link */
#include "work_task.h" /* work_task, work_type */
#include "tcp.h"
#include "pbs_job.h"


hello_container failures;
int svr_tsnodes = 0; 
resource_t next_resource_tag;
char server_name[PBS_MAXSERVERNAME + 1];
all_nodes allnodes;
char *path_nodes;
char *path_nodestate;
char *path_nodenote;
struct addrinfo hints;
char *path_nodes_new;
attribute_def node_attr_def[2];
int svr_clnodes = 0; 
struct server server;
AvlTree ipaddrs = NULL;
int LOGLEVEL = 0;
int svr_totnodes = 0; 
const char *dis_emsg[] = {"No error",
  "Input value too large to convert to this type",
  "Tried to write floating point infinity",
  "Negative sign on an unsigned datum",
  "Input count or value has leading zero",
  "Non-digit found where a digit was expected",
  "Input string has an embedded ASCII NUL",
  "Premature end of message",
  "Unable to malloc enough space for string",
  "Supporting protocol failure",
  "Protocol failure in commit",
  "End of File"
};
dynamic_string *hierarchy_holder;
extern int cray_enabled;


int insert_thing(resizable_array *ra, void *thing)
  {
  fprintf(stderr, "The call to insert_thing needs to be mocked!!\n");
  exit(1);
  }

svrattrl *attrlist_create(char *aname, char *rname, int vsize)
  {
  fprintf(stderr, "The call to attrlist_create needs to be mocked!!\n");
  exit(1);
  }

int remove_thing(resizable_array *ra, void *thing)
  {
  fprintf(stderr, "The call to remove_thing needs to be mocked!!\n");
  exit(1);
  }

AvlTree AVL_delete_node(u_long key, uint16_t port, AvlTree tree)
  {
  fprintf(stderr, "The call to AVL_delete_node needs to be mocked!!\n");
  exit(1);
  }

int add_hash(hash_table_t *ht, int value, void *key)
  {
  fprintf(stderr, "The call to add_hash needs to be mocked!!\n");
  exit(1);
  }

struct work_task *set_task(enum work_type type, long event_id, void (*func)(), void *parm, int get_lock)
  {
  fprintf(stderr, "The call to set_task needs to be mocked!!\n");
  exit(1);
  }

int find_attr(struct attribute_def *attr_def, char *name, int limit)
  {
  fprintf(stderr, "The call to find_attr needs to be mocked!!\n");
  exit(1);
  }

int mgr_set_node_attr(struct pbsnode *pnode, attribute_def *pdef, int limit, svrattrl *plist, int privil, int *bad, void *parent, int mode)
  {
  fprintf(stderr, "The call to mgr_set_node_attr needs to be mocked!!\n");
  exit(1);
  }

void free_prop_list(struct prop *prop)
  {
  fprintf(stderr, "The call to free_prop_list needs to be mocked!!\n");
  exit(1);
  }

int get_value_hash(hash_table_t *ht, void *key)
  {
  char *str = (char *)key;

  if (str == NULL)
    return(-1);
  else if (!strcmp(str, "bob"))
    return(1);
  else if (!strcmp(str, "tom"))
    return(2);
  else
    return(-1);
  }

void *get_next(list_link pl, char *file, int line)
  {
  fprintf(stderr, "The call to get_next needs to be mocked!!\n");
  exit(1);
  }

resizable_array *initialize_resizable_array(int size)
  {
  fprintf(stderr, "The call to initialize_resizable_array needs to be mocked!!\n");
  exit(1);
  }

struct pbsnode *AVL_find(u_long key, uint16_t port, AvlTree tree)
  {
  static struct pbsnode numa;
  static char           buf[20];

  if (key > 2)
    return(NULL);
  else
    {
    sprintf(buf, "%lu", key);
    numa.nd_name = buf;
    return(&numa);
    }
  }

void free_attrlist(tlist_head *pattrlisthead)
  {
  fprintf(stderr, "The call to free_attrlist needs to be mocked!!\n");
  exit(1);
  }

void *next_thing(resizable_array *ra, int *iter)
  {
  fprintf(stderr, "The call to next_thing needs to be mocked!!\n");
  exit(1);
  }

void append_link(tlist_head *head, list_link *new_link, void *pobj)
  {
  fprintf(stderr, "The call to append_link needs to be mocked!!\n");
  exit(1);
  }

hash_table_t *create_hash(int size)
  {
  fprintf(stderr, "The call to create_hash needs to be mocked!!\n");
  exit(1);
  }

char *pbs_strerror(int err)
  {
  fprintf(stderr, "The call to pbs_strerror needs to be mocked!!\n");
  exit(1);
  }

AvlTree AVL_insert(u_long key, uint16_t port, struct pbsnode *node, AvlTree tree)
  {
  fprintf(stderr, "The call to AVL_insert needs to be mocked!!\n");
  exit(1);
  }

int unlock_node(struct pbsnode *the_node, const char *id, char *msg, int logging)
  {
  return(0); 
  }                           

int lock_node(struct pbsnode *the_node, const char *id, char *msg, int logging)
  { 
  return(0); 
  }                           

void *pop_thing(resizable_array *ra)

  {
  return(NULL);
  }

int is_present(resizable_array *ra, void *thing)
  {
  fprintf(stderr, "The call to is_present needs to be mocked!!\n");
  exit(1);                    
  }


void DIS_tcp_setup(int sock)
  {
  fprintf(stderr, "The call to DIS_tcp_setup needs to be mocked!!\n");
  exit(1);                    
  }



int DIS_tcp_wflush(int sock)
  {
  fprintf(stderr, "The call to DIS_tcp_wflush needs to be mocked!!\n");
  exit(1);                    
  }


int diswcs (int stream, const char *value, int len)
  {
  fprintf(stderr, "The call to diswcs needs to be mocked!!\n");
  exit(1);                    
  }


int tcp_connect_sockaddr(struct sockaddr *sa, size_t s)
  {
  fprintf(stderr, "The call to tcp_connect_sockaddr needs to be mocked!!\n");
  exit(1);                    
  }

int diswsi(int sock, int value)
  {
  fprintf(stderr, "The call to diswsi needs to be mocked!!\n");
  exit(1);                    
  }

int get_svr_attr_l(int index, long *l)
  {
  if (index == SRV_ATR_CrayEnabled)
    *l = cray_enabled;

  return(0);
  }

int add_conn(int sock, enum conn_type type, pbs_net_t addr, unsigned int port, unsigned int socktype, void *(*func)(void *))
  {
  return(0);
  }

void close_conn(int sd, int has_mutex)
  {
  }

int get_svr_attr_str(int index, char **str)
  {
  return(0);
  }

int remove_thing_from_index(resizable_array *ra, int index)
  {
  fprintf(stderr, "The call to remove_thing_from_index needs to be mocked!!\n");
  exit(1);
  }

int insert_thing_after(resizable_array *ra, void *thing, int index)
  {
  fprintf(stderr, "The call to insert_thing_after needs to be mocked!!\n");
  exit(1);
  }

int get_addr_info(char *name, struct sockaddr_in *sa_info, int retry)
  {
  return(0);
  }

int is_compose(

  struct tcp_chan *chan,
  char *server_name,
  int   command)

  {
  return(0);
  }

void DIS_tcp_cleanup(struct tcp_chan *chan)
  {
  }

int add_to_login_holder(

  struct pbsnode *pnode)

  {
  return(0);
  }

int append_dynamic_string(

  dynamic_string *ds,
  const char     *str)

  {
  return(0);
  }

dynamic_string *get_dynamic_string(

  int         size,
  const char *str)

  {
  return(NULL);
  }

int login_node_count() 

  {
  return(0);
  }

struct sockaddr_in *get_cached_addrinfo(
    
  char               *hostname)

  {
  return(NULL);
  }

void free_dynamic_string(dynamic_string *ds) {}

job *get_job_from_jobinfo(
    
  struct jobinfo *jp,
  struct pbsnode *pnode)

  {
  return(NULL);
  }

int insert_addr_name_info(
    
  char               *hostname,
  char               *full_hostname,
  struct sockaddr_in *sai)

  {
  return(0);
  }

int unlock_ji_mutex(job *pjob, const char *id, char *msg, int logging)
  {
  return(0);
  }

const char *alps_reporter_feature  = "alps_reporter";
const char *alps_starter_feature   = "alps_starter";
