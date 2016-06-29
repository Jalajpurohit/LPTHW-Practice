class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self,subject,verb,object):
        # remember we take ('noun', 'princess') tuple and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]

    def peek(word_list):
        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None

    def match(word_list,expecting):
       if word_list:
            word = word_list.pop(0)

            if word[0] == expecting:
                return word
            else:
                return None
       else:
            return None

    def skip(word_list,word_type):
       while Sentence.peek(word_list) == word_type:
           Sentence.match(word_list,word_type)

    def parse_verb(word_list):
        Sentence.skip(word_list,'stop')

        if Sentence.peek(word_list) == 'verb':
            return Sentence.match(word_list,'verb')
        else:
            raise ParserError("Expected a verb next.")

    def parse_object(word_list):
        Sentence.skip(word_list,'stop')
        next = Sentence.peek(word_list)

        if next == 'noun':
            return Sentence.match(word_list,'noun')
        if next == 'direction':
            return Sentence.match(word_list,'direction')
        else:
            raise ParserError("Expected a noun or direction next.")

    def parse_subject(word_list,subj):
        verb = Sentence.parse_verb(word_list)
        obj = Sentence.parse_object(word_list)

        return Sentence(subj,verb,obj)

    def parse_sentence(word_list):
        Sentence.skip(word_list,'stop')

        start = Sentence.peek(word_list)

        if start == 'noun':
            subj = Sentence.match(word_list,'noun')
            return Sentence.parse_subject(word_list,subj)
        elif start == 'verb':
            # assume the subject is the player then
            return Sentence.parse_subject(word_list,('noun','player'))
        else:
            raise ParserError("Must start with subject, object, or verb not: %s" % start)