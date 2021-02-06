basic_arith = \
    """
    walker init {
        a = 4 + 4;
        b = 4 * -5;
        c = 4 / 4;  # Returns a floating point number
        d = 4 - 6;
        e = a + b + c + d;
        std.out(a, b, c, d, e);
    }
    """

more_arith = \
    """
    walker init {
        a = 4 ^ 4; b = 9 % 5; std.out(a, b);
    }
    """

compare = \
    """
    walker init {
        a = 5; b = 6;
        std.out(a == b,
                a != b,
                a < b,
                a > b,
                a <= b,
                a >= b,
                a == b-1);
    }
    """

logical = \
    """
    walker init {
        a = true; b = false;
        std.out(a,
                !a,
                a && b,
                a || b,
                a and b,
                a or b,
                !a or b,
                !(a and b));
    }
    """

assignments = \
    """
    walker init {
        a = 4 + 4; std.out(a);
        a += 4 + 4; std.out(a);
        a -= 4 * -5; std.out(a);
        a *= 4 / 4; std.out(a);
        a /= 4 - 6; std.out(a);

        # a := here; std.out(a);
        # Noting existence of copy assign, described later
    }
    """

if_stmt = \
    """
    walker init {
        a = 4; b = 5;
        if(a < b): std.out("Hello!");
    }
    """

else_stmt = \
    """
    walker init {
        a = 4; b = 5;
        if(a == b): std.out("A equals B");
        else: std.out("A is not equal to B");
    }
    """

elif_stmt = \
    """
    walker init {
        a = 4; b = 5;
        if(a == b): std.out("A equals B");
        elif(a > b): std.out("A is greater than B");
        elif(a == b - 1): std.out("A is one less than B");
        elif(a == b - 2): std.out("A is two less than B");
        else: std.out("A is something else");
    }
    """

for_stmt = \
    """
    walker init {
        for i=0 to i<10 by i+=1:
            std.out("Hello", i, "times!");
    }
    """
while_stmt = \
    """
    walker init {
        i = 5;
        while(i>0) {
            std.out("Hello", i, "times!");
            i -= 1;
        }
    }
    """

break_stmt = \
    """
    walker init {
        for i=0 to i<10 by i+=1 {
            std.out("Hello", i, "times!");
            if(i == 6): break;
        }
    }
    """

continue_stmt = \
    """
    walker init {
        i = 5;
        while(i>0) {
            if(i == 3){
                i -= 1; continue;
            }
            std.out("Hello", i, "times!");
            i -= 1;
        }
    }
    """

destroy_disconn = \
    """
    node test {
        has apple;
    }

    walker init{
        node1 = spawn here --> node::test;
        node2 = spawn here --> node::test;
        node1 --> node2;
        std.out(-->);
        destroy node1;
        std.out(-->);
        here !--> node2;
        std.out('1', -->);
    }
    """

array_assign = \
    """
    node test {
        has apple;
    }

    walker init{
        root {
            node1 = spawn here --> node::test;
            node1.apple = [[1,2],[3,4]];
            take node1;
        }
        test {
            a = [[0,0],[0,0]];
            std.out(a);
            a[0] = [1,1];
            std.out(a);
            std.out(here.apple);
            here.apple[0] = [4,5];
            std.out(here.apple);
        }
    }
    """

array_md_assign = \
    """
    node test {
        has apple;
    }

    walker init{
        root {
            node1 = spawn here --> node::test;
            node1.apple = [[1,2],[3,4]];
            take node1;
        }
        test {
            std.out(here.apple);
            here.apple[0][1] = 76;
            std.out(here.apple);
        }
    }
    """

dereference = \
    """
    node test {
        has apple;
    }

    walker init{
        root {
            node1 = spawn here --> node::test;
            std.out(&node1);
        }
    }
    """