.PHONY: clean

# Headers
API_INCLUDES = -Iinclude/api

# Sources
API_SOURCES = $(wildcard src/api/*.c)

CC = gcc
CFLAGS = -g -DLOG_USE_COLOR=1 -Wall

main:
	$(CC) $(CFLAGS)  $(API_INCLUDES) ${API_SOURCES} src/leptonic1.c -pthread -lpigpio -lrt -o bin/leptonic

clean:
	@rm -f *.o
	@rm leptonic
