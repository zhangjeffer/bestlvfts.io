import glob, os
import json

current_user = "demo"

user_pass = {
   "demo": "password"
}

deadlift = {
   "demo": {"02/20/20": ["5.mov", "395lb x 3"],
            "02/10/20": ["4.mov", "495lb x 2"],
            "02/01/20": ["3.mov", "455lb x 1"],
            "01/20/20": ["2.mov", "545lb x 1"],
            "12/02/19": ["1.mov", "410lb x 3"]
   }
}

squat = {
   "demo": {"02/20/20": ["10.mov", "455lb x 1"],
            "02/10/20": ["9.mov", "355lb x 4"],
            "02/01/20": ["8.mov", "405lb x 2"],
            "01/20/20": ["7.mov", "295lb x 4"],
            "12/02/19": ["6.mov", "340lb x 4"]
   }
}

bench = {
   "demo": {"02/20/20": ["15.mov", "225lb x 4"],
            "02/10/20": ["14.mov", "235lb x 3"],
            "02/01/20": ["13.mov", "220lb x 4"],
            "01/20/20": ["12.mov", "245lb x 3"],
            "12/02/19": ["11.mov", "225lb x 4"]
   }
}


def delete_vid(mov):
   squat_dict = squat.get(current_user)
   bench_dict = bench.get(current_user)
   deadlift_dict = deadlift.get(current_user)
   squat_bool = False
   bench_bool = False
   deadlift_bool = False
   delete_date = None

   for key,val in squat_dict.items():
      if (val[0] == mov):
         delete_date = key
         squat_bool = True

   for key,val in bench_dict.items():
      if (val[0] == mov):
         delete_date = key
         bench_bool = True

   for key,val in deadlift_dict.items():
      if (val[0] == mov):
         delete_date = key
         deadlift_bool = True

   if squat_bool:
      del squat.get(current_user)[delete_date]
   elif bench_bool:
      del bench.get(current_user)[delete_date]
   elif deadlift_bool:
      del deadlift.get(current_user)[delete_date]
   else:
      pass

def validateUser(username, password):
   validate_pass = user_pass.get(username)
   if validate_pass is not None:
      if password == validate_pass:
         current_user = username
         return "true"
   user_pass[username] = password
   return "false"


def printDeadliftJson():
   y = json.dumps(deadlift.get(current_user))
   return y


def printSquatJson():
   y = json.dumps(squat.get(current_user))
   return y


def printBenchJson():
   y = json.dumps(bench.get(current_user))
   return y

