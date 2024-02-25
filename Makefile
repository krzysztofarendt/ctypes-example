.PHONY: clean


SRC_DIR=ctexample/src
BIN_DIR=bin
LIB_DIR=ctexample/library


clean:
	-rm $(BIN_DIR)/example.exe
	-rm $(LIB_DIR)/libfun.so

example.exe:
	gcc -o $(BIN_DIR)/example.exe $(SRC_DIR)/main.c $(SRC_DIR)/fun.c

libfun.so:
	-mkdir $(LIB_DIR)
	gcc -fPIC -c $(SRC_DIR)/fun.c -o $(LIB_DIR)/fun.o
	gcc -shared -o $(LIB_DIR)/libfun.so $(LIB_DIR)/fun.o
	rm $(LIB_DIR)/fun.o
