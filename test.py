import redis

r = redis.StrictRedis(host='192.168.1.112', port=6379, db=0)
#
# pipe = r.pipeline()
#
# pipe.set('test', 'la')
# pipe.set('hehe', 'pp')
#
# pipe.delete('test')
# pipe.delete('hehe')
# pipe.execute()

print r.get('test')
print r.get('hehe')