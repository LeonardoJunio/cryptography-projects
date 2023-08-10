CXX = gcc
CXXFLAGS = -Wall -Wextra -Wpedantic -std=c17

SRCDIR = src
BINDIR = bin

SRCS = $(wildcard $(SRCDIR)/*/*.c)
OBJS = $(patsubst $(SRCDIR)/%,$(BINDIR)/%,$(SRCS:.c=.o))

.PHONY: all clean

all: $(BINDIR)/app

$(BINDIR)/app: $(OBJS)
	$(CXX) $(LDFLAGS) $^ -o $@

$(BINDIR)/%.o: $(SRCDIR)/%.c | $(BINDIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(BINDIR):
	mkdir -p $(BINDIR)

clean:
	$(RM) -r $(BINDIR)
