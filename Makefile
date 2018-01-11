build:
	docker build -t agrrh/isspass:dev .

publish: build
	docker push agrrh/isspass:dev
	docker push agrrh/isspass
