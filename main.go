package main

func main() {
	go a()
	go b()
	// prevent the program from terminating, ignore for now
	// select {}
}

func a() {
	go aa()
	go ab()
}

func aa() {
	println("aa")
}

func ab() {
	println("ab")
}

func b() {
	go ba()
	go bb()
}

func ba() {
	println("ba")
}

func bb() {
	println("bb")
}
