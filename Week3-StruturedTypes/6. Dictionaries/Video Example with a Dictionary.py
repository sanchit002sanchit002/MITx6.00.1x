'''Functions to analyze song lyrics
'''

beatles_heyjude_lyrics = "Hey Jude, don't make it bad Take a sad song and make it better Remember to let her into your heart Then you can start to make it better Hey Jude, don't be afraid You were made to go out and get her The minute you let her under your skin Then you begin to make it better And anytime you feel the pain, hey Jude, refrain Don't carry the world upon your shoulders For well you know that it's a fool who plays it cool By making his world a little colder Nah nah nah nah nah nah nah nah nah Hey Jude, don't let me down You have found her, now go and get her Remember to let her into your heart Then you can start to make it better So let it out and let it in, hey Jude, begin You're waiting for someone to perform with And don't you know that it's just you, hey Jude, you'll do The movement you need is on your shoulder Nah nah nah nah nah nah nah nah nah yeah Hey Jude, don't make it bad Take a sad song and make it better Remember to let her under your skin Then you'll begin to make it Better better better better better better, oh"
#test code 
#print(beatles_heyjude_lyrics)

beatles_heyjude_lyrics_list=beatles_heyjude_lyrics.split(' ')
#test code
#print(beatles_heyjude_lyrics_list)

def lyrics_to_frequencies(lyrics) :
    '''find song each word counts
    '''
    myDict = {}
    for word in lyrics :
        if word in myDict :
            myDict[word] += 1
        else :
            myDict[word] = 1
    return myDict
#test code
print (lyrics_to_frequencies(beatles_heyjude_lyrics_list))


def most_common_words(myDict) :
    '''find song most common word
    '''
    values = myDict.values()
    best = max(values)
    word = []
    for k in myDict :
        if myDict[k] == best :
            word.append(k)
    return(word, best)
#test code
print (most_common_words(lyrics_to_frequencies(beatles_heyjude_lyrics_list)))

def words_often(freqs, minTimes) :
    ''' find song most common word  >minTimes
    '''
    result = []
    done = False
    while not done :
        temp = (most_common_words(freqs))
        if temp[1] >= minTimes :
            result.append(temp)
            for w in temp[0] :
                del(freqs[w])
        else:
            done = True
    return result

#test code
print (words_often(lyrics_to_frequencies(beatles_heyjude_lyrics_list),5))