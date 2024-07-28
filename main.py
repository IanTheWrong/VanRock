from Data import data

f = data()
f.load_json_data()
f.save_json_data()
print(f.fetch_json_data("GME"))