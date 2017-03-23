a=int(raw_input("Which script do you want to run?\nEnter 1 for students_to_teacher\n Enter 2 for battleship\n Enter 3 for exam_stats "))
if a==1:
    import students_to_teacher
elif a==2:
    import battleship
elif a==3:
    import exam_stats
else:
    print "wrong choice"