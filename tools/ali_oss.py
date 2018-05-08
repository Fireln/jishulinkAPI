import oss2
from data.data import eve
import uuid


class AliOss(object):

    def login(self):
        return oss2.Auth(eve.ali_oss.get("AK"), eve.ali_oss.get("AKS"))

    def bucket_list(self, auth):
        service = oss2.Service(auth, "oss.hangzhou.com")
        print([b.name for b in oss2.BucketIterator(service)])

    def get_bucket(self, auth):
        return oss2.Bucket(auth, eve.ali_oss.get("endpoint"), eve.ali_oss.get("bucket"))

    # def create_bucket(self):
    #     return oss2.Bucket(self.auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'fireln-hangzou')

    def put_img(self, path, bucket):
        bucket.put_object_from_file('{}.png'.format(uuid.uuid1()), path)


if __name__ == '__main__':
    t = AliOss()
    auth = t.login()
    bucket = t.get_bucket(auth)
    t.put_img(r"D:\pycharm\jishulinktest\data\data\static\imgs\test.png", bucket)
