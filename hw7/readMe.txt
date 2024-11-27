Instructions:
	install dependencies:
		pycryptodomex: sudo apt install python3-pycryptodome
		
	running:
		put data file in info folder
		
		python3 rainbow.py n salt
			int n - number of characters in unhashed password
			bool salt - with or without salt 1:0
		
			prompt for file: 'name of file'
				- note: program will add txt file type
		
		wait while program is working...

	test files:
		part 1 & 2 run with n = 4
		part 3 & 4 run with n = 3

		part 1 & 3 run with salt = 0
		part 2 & 4 run with salt = 1
