import unittest
import datetime
from datetime import timedelta
from core.filters_internals import *

    
def generate_mail(days_ago: int, sender: str = "sender@example.com", subject: str = "Subject"):
    dt = datetime.now() - timedelta(days=days_ago)
    return {
        "date": dt.strftime("%Y-%m-%d %H:%M:%S"),  
        "from": sender,
        "subject": subject
    }


class TestFilterInternals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.today_mail = generate_mail(0)
        cls.yesterday_mail = generate_mail(1)
        cls.week_old_mail = generate_mail(7)
        cls.month_old_mail = generate_mail(30)
        cls.old_mail = generate_mail(100)

        cls.seen = [cls.today_mail, cls.yesterday_mail]
        cls.unseen = [cls.week_old_mail, cls.month_old_mail, cls.old_mail]


    @classmethod
    def tearDownClass(cls):
        del cls.today_mail
        del cls.yesterday_mail
        del cls.week_old_mail
        del cls.month_old_mail
        del cls.old_mail
        del cls.seen
        del cls.unseen

    
    def test_filter_today(self):
        result = filter_today(self.seen, self.unseen)
        self.assertIn(self.today_mail, result)
        self.assertNotIn(self.yesterday_mail, result)

    def test_filter_week(self):
        result = filter_week(self.seen, self.unseen)
        self.assertIn(self.today_mail, result)
        self.assertIn(self.yesterday_mail, result)
        self.assertIn(self.week_old_mail, result)
        self.assertNotIn(self.month_old_mail, result)

    def test_filter_month(self):
        result = filter_month(self.seen, self.unseen)
        self.assertIn(self.month_old_mail, result)
        self.assertIn(self.week_old_mail, result)
        self.assertIn(self.today_mail, result)
        self.assertNotIn(self.old_mail, result)

    def test_filter_custom_range(self):
        start = date.today() - timedelta(days=10)
        end = date.today()
        result = filter_custom_range(self.seen + self.unseen, start, end)
        self.assertIn(self.today_mail, result)
        self.assertIn(self.yesterday_mail, result)
        self.assertNotIn(self.old_mail, result)

    def test_filter_by_from(self):
        filter_ = {"from_filter": "sender"}
        result = filter_mails(filter_, self.seen, self.unseen)
        for mail in result:
            self.assertIn("sender", mail["from"])

    def test_filter_by_subject(self):
        filter_ = {"subject_filter": "Subject"}
        result = filter_mails(filter_, self.seen, self.unseen)
        for mail in result:
            self.assertIn("Subject", mail["subject"])

    def test_list_senders(self):
        mails = self.seen + self.unseen
        senders = list_senders(mails)
        self.assertIn("sender@example.com", senders)
        self.assertIsInstance(senders, list)


if __name__ == '__main__':
    unittest.main()