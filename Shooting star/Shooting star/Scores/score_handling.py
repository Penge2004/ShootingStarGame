def get_best_score():
    bestscore_file = open('best_score.txt','r')
    bestscore = bestscore_file.read()
    bestscore_file.close()
    return bestscore

def save_new_best(new_best):
    bestscore_file = open('best_score.txt', 'w')
    bestscore_file.write(new_best)
    bestscore_file.close()