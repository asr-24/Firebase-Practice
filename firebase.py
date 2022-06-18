from firebase_admin import db
import firebase_admin as fa
import json


credentials = fa.credentials.Certificate("C:\\Users\\10aru\\Documents\\work22\\python\\FirebasePractice\\practice-db-1-cbfbe-firebase-adminsdk-k3swz-82a54b8c4a.json")
default_app = fa.initialize_app(credentials, {
    'databaseURL' : "https://practice-db-1-cbfbe-default-rtdb.asia-southeast1.firebasedatabase.app"
    })

"""
ref = db.reference("/")

with open("database_1.json", "r") as f:
    contents = json.load(f)

ref.set(contents)

"""

ref = db.reference("/")
ref.set({
	"Books":
	{
		"Best_Sellers": -1
	}
})

ref = db.reference("/Books/Best_Sellers")

with open("database_1.json", "r") as f:
	file_contents = json.load(f)

#print(file_contents)

for key, value in file_contents.items():
	ref.push().set(value)

ref = db.reference("/Books/Best_Sellers/")

best_sellers = ref.get()
#print(best_sellers)


for key, value in best_sellers.items():
	print(key)
	print(value, end = "\n\n")
	

"""
for key, value in best_sellers.items():
	if(value["Author"] == "J.R.R. Tolkien"):
		ref.child(key).update({"Price":80})
		
		


"""