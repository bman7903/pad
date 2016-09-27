#!/usr/bin/env python

ml_db      = 'pad'

ml_uniq    = 'ds017231'
ml_port    = '17231'

mail_col   = 'email'
mail_usr   = 'aboy55'
mail_pwd   = 'alongpassword'


mapi_key   = 'rJ1wItpCy5niBlyMBSQs4jG6Rxo1u8IR'


def mlab( proc ):
  def mldb():
     return ml_db
  def mailcol():
     return mail_col
  def mlkey():
     return mapi_key
  def mailuser():
     return maill_user
  def mailpwd():
     return mail_pwd
  def mailusr():
     return mail_usr
  def mluniq():
     return ml_uniq
  def mlport():
     return ml_port
  t = eval( proc )
  return t()

