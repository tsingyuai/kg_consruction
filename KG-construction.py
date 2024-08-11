import pandas as pd
import networkx as nx

# 读取Excel文件
raw_data_df = pd.read_excel('groudtruth_szy-20240726-V2.xlsx')

# 创建一个空的有向图G
G = nx.DiGraph()

# 添加节点
# 添加'Polymer'相关结点
for node_id in raw_data_df['Polymer.Name'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Polymer.Name')


# 添加'Monomer'相关结点
for node_id in raw_data_df['Monomers1.Name'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Monomers.Name')

for node_id in raw_data_df['Monomers1.SMILES'].unique():
    if pd.notna(node_id):    
        G.add_node(node_id,label='Monomers.SMILES')

for node_id in raw_data_df['Monomers1.CAS'].unique():
    if pd.notna(node_id):    
        G.add_node(node_id,label='Monomers.CAS')

for node_id in raw_data_df['Monomers2.Name'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Monomers.Name')

for node_id in raw_data_df['Monomers2.SMILES'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Monomers.SMILES')

for node_id in raw_data_df['Monomers2.CAS'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Monomers.CAS')

for node_id in raw_data_df['Monomers3.Name'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Monomers.Name')

for node_id in raw_data_df['Monomers3.SMILES'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Monomers.SMILES')

for node_id in raw_data_df['Monomers3.CAS'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Monomers.CAS')

# 添加'Salt'相关结点
for node_id in raw_data_df['Salts1.Name'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Salts.Name')

for node_id in raw_data_df['Salts1.SMILES'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Salts.SMILES')

for node_id in raw_data_df['Salts1.CAS'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Salts.CAS')

for node_id in raw_data_df['Salts2.Name'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Salts.Name')

for node_id in raw_data_df['Salts2.SMILES'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Salts.SMILES')

for node_id in raw_data_df['Salts2.CAS'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Salts.CAS')


# 对于我们的数据集需要加序号，此处针对'ground_truth'不需要添加序号
# for node_id in raw_data_df['Polymerization.Activation_energy.Description'].unique():
#     if pd.notna(node_id):
#         G.add_node(node_id,label='Polymerization.Activation_energy.Description')


# 'Experiment_Methods'构建结点但是不一定建模到图中
# for node_id in raw_data_df['Experiment_Methods'].unique():
#     if pd.notna(node_id):
#         G.add_node(node_id,label='Experiment_Methods')

# for node_id in raw_data_df['Mechanism'].unique():
#     if pd.notna(node_id):
#         G.add_node(node_id,label='Mechanism')

# SPE结点相关指标   # Tg
for node_id in raw_data_df['Transference_Number.Value'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Transference_Number')

for node_id in raw_data_df['Glass_transition_temperature1.Name'].unique():
    if pd.notna(node_id):
        G.add_node(node_id,label='Glass_transition_temperature.Name')

for index, row in raw_data_df.iterrows():
    if pd.notna(row['Glass_transition_temperature1.Name']):
        if pd.notna(row['Glass_transition_temperature1.Value']):
            G.add_node(row['Glass_transition_temperature1.Value'], 
                       label='Glass_transition_temperature.Value', 
                       unit=str(row['Glass_transition_temperature1.Unit']) if pd.notna(row['Glass_transition_temperature1.Unit']) else None,
                       conditon=f'{row["Glass_transition_temperature1.Name"]}')
        else:
            G.add_node(row['Glass_transition_temperature1.Name'],
                       label='Glass_transition_temperature.Name')


    if pd.notna(row['Tensile_Strength.Value']):
        G.add_node(row['Tensile_Strength.Value'], label='Tensile_Strength.Value', unit=str(row['Tensile_Strength.Unit']) if pd.notna(row['Tensile_Strength.Unit']) else None)

    if pd.notna(row['Critical_Current_Density.Value']):
        G.add_node(row['Critical_Current_Density.Value'], label='Critical_Current_Density.Value', unit=str(row['Critical_Current_Density.Unit']) if pd.notna(row['Critical_Current_Density.Unit']) else None)

    if pd.notna(row['Electrochemical_Window.Value']):
        G.add_node(row['Electrochemical_Window.Value'], 
                   label='Electrochemical_Window.Value',
                   unit=str(row['Tensile_Strength.Unit']) if pd.notna(row['Tensile_Strength.Unit']) else None)
    if pd.notna(row['Transference_Number.Value']):
        G.add_node(row['Transference_Number.Value'], 
                   label='Transference_Number.Value', 
                   unit=str(row['Transference_Number.Unit']) if pd.notna(row['Transference_Number.Unit']) else None)
    if pd.notna(row['Initiators1.Concentration.Value']):
        G.add_node(row['Initiators1.Concentration.Value'], label='Initiators.Concentration.Value', unit=str(row['Initiators1.Concentration.Unit']) if pd.notna(row['Initiators1.Concentration.Unit']) else None)

    if pd.notna(row['Polymer.Molecular_weight.Value']):
        G.add_node(row['Polymer.Molecular_weight.Value'], label='Polymer.Molecular_weight.Value', unit=str(row['Polymer.Molecular_weight.Unit']) if pd.notna(row['Polymer.Molecular_weight.Unit']) else None)

    if pd.notna(row['Polymerization.Temperature.Value']):
        G.add_node(row['Polymerization.Temperature.Value'], label='Polymerization.Temperature.Value', unit=str(row['Polymerization.Temperature.Unit']) if pd.notna(row['Polymerization.Temperature.Unit']) else None)

    if pd.notna(row['Polymerization.Time.Value']):
        G.add_node(row['Polymerization.Time.Value'], label='Polymerization.Time.Value', unit=str(row['Polymerization.Time.Unit']) if pd.notna(row['Polymerization.Time.Unit']) else None)

    # if pd.notna(row['Polymerization.Activation_energy.Value']):
    #     G.add_node(row['Polymerization.Activation_energy.Value'], label='Polymerization.Activation_energy.Value', unit=str(row['Polymerization1.Activation_energy.Unit']) if pd.notna(row['Polymerization1.Activation_energy.Unit']) else None)



# 针对我们的测试集如果有多个Tg值此处可以增加
# for node_id in raw_data_df['Glass_transition_temperature2.Name'].unique():
#     if pd.notna(node_id):
#         G.add_node(node_id,label='Glass_transition_temperature.Name')


# 离子导率相关
for index, row in raw_data_df.iterrows():
    if pd.notna(row['Conductivity.Value']):
        G.add_node(row['Conductivity.Value'], label='Conductivity.Value', unit=str(row['Conductivity.Unit']) if pd.notna(row['Conductivity.Unit']) else None)
    if pd.notna(row['Conductivity.Temperature.Value']):
        G.add_node(row['Conductivity.Temperature.Value'], label='Polymer.Concentration.Value', unit=str(row['Conductivity.Temperature.Unit']) if pd.notna(row['Polymer.Concentration.Unit']) else None)

# 合并完全相同的节点
unique_nodes = {}
for node, data in G.nodes(data=True):
    node_key = (node, data.get('label'), data.get('unit'))
    if node_key in unique_nodes:
        nx.contracted_nodes(G, unique_nodes[node_key], node, self_loops=False)
    else:
        unique_nodes[node_key] = node



# 创建虚结点
# 'SPE'
for url, group in raw_data_df.groupby('url'):
    dummy_node_id = f'SPE_{url}'
    G.add_node(dummy_node_id, label='dummy_SPE')
    for index, row in group.iterrows():
        if not G.has_edge(row['Salts1.Name'], dummy_node_id):
            G.add_edge(row['Salts1.Name'], dummy_node_id,
                       label='Basis')
                       # condition=f'{row['Salt.Concentration']}'
        if not G.has_edge(row['Salts2.Name'], dummy_node_id):
            G.add_edge(row['Salts2.Name'], dummy_node_id)
        if not G.has_edge(row['Polymer.Name'], dummy_node_id):
            G.add_edge(row['Polymer.Name'], dummy_node_id,
                       label='Basis',
                       condition=f'Concentration:{row["Polymer.Concentration.Value"]}{row["Polymer.Concentration.Unit"]},Weight_Ratio:{row["Polymer.Component.Weight_Ratio"]},Molar_Ratio:{row["Polymer.Component.Molar_Ratio"]}')
        if not G.has_edge(dummy_node_id, row['Conductivity.Value']):
            G.add_edge(dummy_node_id, row['Conductivity.Value'],
                       label='Property',
                       condition=f'{row["Conductivity.Temperature.Value"]}{row["Conductivity.Temperature.Unit"]}')
        if not G.has_edge(dummy_node_id, row['Electrochemical_Window.Value']):
            G.add_edge(dummy_node_id, row['Electrochemical_Window.Value'],
                       label='Property',
                       condition=f"{row['Electrochemical_Window.Temperature.Value']}{str(row['Electrochemical_Window.Temperature.Unit']) if pd.notna(row['Electrochemical_Window.Temperature.Unit']) else None}")
        if not G.has_edge(dummy_node_id, row['Transference_Number.Value']):
            G.add_edge(dummy_node_id, row['Transference_Number.Value'],
                       label='Property',
                       condition=f"{row['Transference_Number.Temperature.Value']} {str(row['Transference_Number.Temperature.Unit']) if pd.notna(row['Transference_Number.Temperature.Unit']) else None}")
        if not G.has_edge(dummy_node_id, row['Critical_Current_Density.Value']):
            G.add_edge(dummy_node_id, row['Critical_Current_Density.Value'],label='Property')



# 添加边
for index, row in raw_data_df.iterrows():
    # Monomer
    G.add_edge(row['Monomers1.Name'], row['Monomers1.SMILES'],label='Description')
    G.add_edge(row['Monomers1.Name'], row['Monomers1.CAS'],label='Description')
    G.add_edge(row['Monomers1.Name'],row['Polymer.Name'],
               label="Polymerzation",
               condition=f"{row['Initiators1.Name']} {row['Initiators1.Concentration.Value']}{row['Initiators1.Concentration.Unit']},{row['Polymerization.Temperature.Value']}{row['Polymerization.Temperature.Unit']},{row['Polymerization.Time.Value']}{row['Polymerization.Time.Unit']}")

    G.add_edge(row['Monomers2.Name'], row['Monomers2.SMILES'],label='Description')
    G.add_edge(row['Monomers2.Name'], row['Monomers2.CAS'],label='Description')
    # Polymer
    G.add_edge(row['Polymer.Name'], row['Tensile_Strength.Value'],label='Property')

    # Salt
    G.add_edge(row['Salts1.Name'], row['Salts1.SMILES'],label='Description')
    G.add_edge(row['Salts1.Name'], row['Salts1.CAS'],label='Description')
    G.add_edge(row['Salts1.Name'],row['Conductivity.Value'],label='Property',condition=f'{row["Conductivity.Ion"]}')
    G.add_edge(row['Salts2.Name'], row['Salts2.SMILES'],label='Description')
    G.add_edge(row['Salts2.Name'], row['Salts2.CAS'],label='Description')




# 显示图中的节点及其属性
# print("Nodes and their attributes:")
# print(G.nodes(data=True))

# 显示图中的边及其属性（如果有）
# print("\nEdges and their attributes:")
# print(G.edges(data=True))

# 删除 Node、label 和 unit 都为空的节点（保留虚结点）
nodes_to_remove = [node for node, data in G.nodes(data=True) if (not node or pd.isna(node)) and all(pd.isna(v) or v == "" for v in data.values())]
G.remove_nodes_from(nodes_to_remove)

# 显示节点和边的数量
print("\nNumber of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())


node_data = []
for node, data in G.nodes(data=True):
     node_data.append({"Node": node, **data})

 # 获取边的信息
edge_data = []
for u, v, data in G.edges(data=True):
    edge_data.append({"Source": u, "Target": v, **data})

# 转换为 DataFrame 并保存到 CSV
node_df = pd.DataFrame(node_data)
edge_df = pd.DataFrame(edge_data)

# 确保所有在边数据中引用的节点都在节点数据中
edge_nodes = set(edge_df['Source']).union(set(edge_df['Target']))
node_nodes = set(node_df['Node'])
missing_nodes = edge_nodes - node_nodes

if missing_nodes:
    print(f"Adding {len(missing_nodes)} missing nodes to node data.")
    for node in missing_nodes:
        node_data.append({"Node": node})  # 添加缺失的节点，没有其他属性
    node_df = pd.DataFrame(node_data)

node_df.to_csv("nodes.csv", index=False)
edge_df.to_csv("edges.csv", index=False)

print("Node and edge data saved to CSV.")
print(f"Total nodes in node_df: {len(node_df)}")
print(f"Total edges in edge_df: {len(edge_df)}")

