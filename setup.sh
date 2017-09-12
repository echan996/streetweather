if  [[ "$OSTYPE"=="darwin"* ]]; then
	#mac installs
	brew install python
	brew install pip
elif [[ "$OSTYPE"=="linux"* ]]; then
	# linux installs
	sudo apt-get install python2.7
	wget https://bootstrap.pypa.io/get-pip.py
	python get-pip.py
fi
 