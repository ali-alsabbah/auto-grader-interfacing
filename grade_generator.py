from set_dictionaries import set2
import subprocess

submit_command = "/pub/cs/dcox/cs110a/submit"
exercise_set = set2
exercise_number = "2"

grades_file = open("grades_for_set2.txt", "w+")

for i in exercise_set:
    total_score = 0

    if not exercise_set[i]:
        continue

    print(i)
    grades_file.write(i + '\n' + '\n')

    for j in range(len(exercise_set[i])):
        try:
            output = subprocess.check_output([submit_command, f"{exercise_number}.{j}", exercise_set[i][j]])
        except Exception as e:
            print("error\n")
            grades_file.write("error\n")
            continue
        output = output.decode('utf-8')
        output = output.split('\n')
        output.reverse()

        for line in output:
            if "Score on exercise" in line:
                print(line)
                grades_file.write(line + '\n')
                total_score += int(line[-1])
                break

    print("\nTotal Score: " + str(total_score) + '\n')
    grades_file.write("\nTotal Score: " + str(total_score) + '\n')
    grades_file.write('\n')

grades_file.close()
