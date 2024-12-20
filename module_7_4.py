team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6

#Использование %
s1 = 'В команде %s участников: %d!'
print(s1 %(team1, team1_num))
print(s1 %(team2, team2_num))

#Использование %
# team1_num = 5
# print('В команде Мастера кода участников: %d ! ' % team1_num)

# team1_num = 5
# team2_num = 6
# print('В команде Мастера кода участников: %d и %d !' % (team1_num, team2_num))

#Использование format()
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
s2 = 'Команда {team} решила задач: {score}!'
s3 = '{team} решили задачи за {time:.1f} с!'
print(s2.format(team = team1, score = score_1))
print(s3.format(team = team1, time = team1_time))
print(s2.format(team = team2, score = score_2))
print(s3.format(team = team2, time = team2_time))

# print('Команда Волшебники данных решила задач: {}!'.format(score_2))
# team1_time = 18015.2
# print(' Волшебники данных решили задачи за {tt} с !'.format(tt = team1_time))

#Использование f-строк
score_1, score_2 = 40, 42
print(f'Команды решили {score_1} и {score_2} задач.')

def challenge_result(team1, team2, score_1, score_2, team1_time, team2_time):
    if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
        result = f'Победа команды {team1}!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
        result = f'Победа команды {team2}!'
    else:
        result = 'Ничья!'
    return result

print(f'Результат битвы: {challenge_result(team1, team2, score_1, score_2, team1_time, team2_time)}')
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!.')