from education import permission_hook

perm_dic= {

    #'crm_table_index': ['table_index', 'GET', [], {'source':'qq'}, ],  # 可以查看CRM APP里所有数据库表
    'education_table_change': ['data_change', 'GET', [], {},permission_hook.view_my_own_customers],  # 可以查看每张表里所有的数据
    'education_list_delete': ['data_delete', 'GET', [], {}],  # 可以访问表里每条数据的修改页
    'education_table_save': ['data_change', 'POST', [], {},]
    # 可以查看每张表里所有的数据

}



