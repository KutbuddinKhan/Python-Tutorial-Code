def function_name_print(a,b,c,d,e):
    print(a,b,c,d,e)

function_name_print('kkhan', 'kasim', 'ahsan', 'aslam','aafi')


# Args
def funargs(normal1, *args, **kwargs):
    print(normal1)

    for item in args:
        print(item)

    print("\nNow I would like to intorduce some falto log")

    for key, value in kwargs.items():
        print(f"{key} is a {value}")

arg = ['kkhan', 'kasim', 'ahsan', 'aslam','aafi']
normal = "I am a normal arguments and the students are:"
kw = {"kkhan":"Monitor", "Kasim":"Trainer",
      "Aslam":"Chapri Boy"}
funargs(normal, *arg, **kw)