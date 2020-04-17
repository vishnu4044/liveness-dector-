import os

print("Select operation.")
print("1.video file of fake")
print("2.video file of real")
print("3.train module")
print("4.face module")
choice = input("Enter choice(1/2/3/4): ")


if choice == '1':
   os.chdir("C:/Users/vishnu sai/Desktop/liveness-detection-opencv/videos")
   os.system('cmd /c "python real.py"')
   os.chdir("C:/Users/vishnu sai/Desktop/liveness-detection-opencv")
   os.system('cmd /c "python gather_examples.py --input videos/fake.mp4 --output dataset/fake --detector face_detector --skip 1"')

elif choice == '2':
   os.chdir("C:/Users/vishnu sai/Desktop/liveness-detection-opencv")
   os.system( 'cmd /c "python gather_examples.py --input videos/real.mp4 --output dataset/real --detector face_detector --skip 4"')

elif choice == '3':
   os.chdir("C:/Users/vishnu sai/Desktop/liveness-detection-opencv")
   os.system('cmd /c "python train_liveness.py --dataset dataset --model liveness.model --le le.pickle --plot plot.png"')

elif choice == '4':
   os.chdir("C:/Users/vishnu sai/Desktop/liveness-detection-opencv")
   os.system('cmd /c "python liveness_demo.py --model liveness.model --le le.pickle --detector face_detector"')
else:
   print("Invalid input enter properly")
   print("Select operation.")
   print("1.video file of fake")
   print("2.video file of real")
   print("3.train module")
   print("4.face module")


   choice = input("Enter choice(1/2/3/4): ")