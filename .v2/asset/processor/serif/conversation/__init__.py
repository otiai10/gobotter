
class Echo:
  @classmethod
  def process(self, resource, args):
    # {{{ replace ??? or any processing
    text = '@' + args['user']['screen_name'] + ' '#TODO : DRY? or It's needed?
    text += resource.replace('%{text_given}', args['text_given'])
    # }}}
    return text