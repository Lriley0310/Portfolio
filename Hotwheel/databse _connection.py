#import statements
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Allowing credentials to firebase admin
cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
	'databaseURL': 'https://hotwheel-databse-default-rtdb.firebaseio.com/'
})

#Setting reference point to the first /
ref = db.reference('/')

#Menue set up that allows you to add or delete
while True:
	print('1. Add Car')
	print('2. Delete Car')
	print('3. Update Car')
	print('4. Exit')
	choice = input("Enter your choice (#): ")

#if statement for user input and decides what to do based on input
	if choice == '1':
		year = input("What was the year the Hotwheel was manufactured?:")
		color = input("What are the colors on the Hotwheel?:")
		make = input('What is the make of the Hotwheel?:')
		model = input('What is the model of the Hotwheel?:')
		title = (f'{make.upper()} {model.upper()}')
		#adds / in between each color given
		words = color.split()
		fixed_color = '/'.join(words)

		#this is the statement that adds user inputs into the database
		ref.push({
				'Year Manufactured': year.title(),
				'Make': make.title(),
				'Model' : model.title(),
				'Color' : fixed_color.title(),
				'Title' : title.title(),
})
	#this is the statement that deletes the inputed hotwheel
	elif choice == '2':
		deltitle = input('Which car would you like to delete?(Must enter individual ID):')
		ref.child(deltitle).delete()
	
	#This is to update individual childs elements
	elif choice == '3':
		change = input('What do you want to Change?: ')
		fixchange = change.title()
		name = input('What car would you like to update?(Must Input individual Key):')
		if fixchange == 'Year':
			yearup = input("What was the year the Hotwheel was manufactured?:")
			ref.child(name).update({"Year Manufactured" : yearup})
		elif fixchange == 'Color':
			colorup = input('What is the updated Color?:')
			words2 = colorup.split()
			fixed_color2 = '/'.join(words2)
			ref.child(name).update({'Color' : fixed_color2.title()})
		elif fixchange == 'Make':
			makeup = input('What is the updated Make?:')
			ref.child(name).update({'Make' : makeup})
		elif fixchange == 'Model':
			modelup = input('What is the updated Model?:')
			ref.child(name).update({'Model' : modelup})
		elif fixchange == 'Title':
			makeup = input('What is the updated Make?:')
			modelup = input('What is the updated Model?:')
			titleup = (f'{makeup.upper()} {modelup.upper()}')
			ref.child(name).update({'Title' : titleup})

	#this is the one that exits the loop statement
	elif choice == '4':
		print('Thnk you!')
		break
	else:
		print("Invalid choice. Please try again.")


