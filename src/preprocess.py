import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#As a side note, these are manually assigned column names from the official NSL-KDD column list.
cols = [
"duration","protocol_type","service","flag","src_bytes","dst_bytes","land",
"wrong_fragment","urgent","hot","num_failed_logins","logged_in",
"num_compromised","root_shell","su_attempted","num_root",
"num_file_creations","num_shells","num_access_files","num_outbound_cmds",
"is_host_login","is_guest_login","count","srv_count","serror_rate",
"srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
"diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
"dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
"dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
"dst_host_rerror_rate","dst_host_srv_rerror_rate","label","difficulty"
]

df = pd.read_csv("data/KDDTrain+_20Percent.txt", names=cols)

# since the last column is just a difficulty score given by the dataset creators, it will be dropped
# as it is irrelavent

df = df.drop("difficulty", axis=1)

#further cleaning steps:

#convert the labels to binary
df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)

#Encode the categorical features with one-hot encoding
df = pd.get_dummies(df, columns=['protocol_type', 'service', 'flag'])

#normalize the data to fit the normal distribution
scaler = StandardScaler()
X = df.drop('label', axis=1)
y = df['label']

X_scaled = scaler.fit_transform(X)

#now implement the train and testing split to ensure model generalizes well to new data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)