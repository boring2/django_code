from django.test import TestCase
from django.utils import timezone
from polls.models import Poll
import datetime
from django.core.urlresolvers import reverse
# Create your tests here.
class PollMethodTest(TestCase):
	def test_was_published_recently_with_future_poll(self):
		future_poll = Poll.objects.create(pub_date=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_poll.was_published_recently(),False)

	def test_was_published_recently_with_old_poll(self):
		old_poll = Poll.objects.create(pub_date=timezone.now() - datetime.timedelta(days=2))
		self.assertEqual(old_poll.was_published_recently(),False)

	def test_was_published_recently_with_now_poll(self):
		now_poll = Poll.objects.create(pub_date=timezone.now() - datetime.timedelta(hours=3))
		self.assertEqual(now_poll.was_published_recently(),True)

def create_poll(question, days):
	return Poll.objects.create(question=question, pub_date=timezone.now()+datetime.timedelta(days=days))
class PollViewTests(TestCase):
	def test_index_view_with_no_polls(self):
		response = self.client.get(reverse('polls:index'))
		print 'response',response.context['lastest_polls_list']
		self.assertEqual(response.status_code,200)
		self.assertContains(response,'No polls are available.')
		self.assertQuerysetEqual(response.context['lastest_polls_list'],[])	
		
	def test_index_view_with_a_past_poll(self):
		create_poll('past poll.',days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['lastest_polls_list'],['<Poll: past poll.>'])

	def test_index_view_with_a_future_poll(self):
		create_poll('future poll.',days=30)
		response = self.client.get(reverse('polls:index'))
		#self.assertEqual(response.status_code,404)
		self.assertContains(response,'No polls are available.')
		self.assertQuerysetEqual(response.context['lastest_polls_list'],[])

	def test_index_view_with_future_poll_and_past_poll(self):
		create_poll('future poll.',days=30)
		create_poll('past poll.',days=-5)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['lastest_polls_list'],['<Poll: past poll.>'])
		
class PollDetailsTest(TestCase):
	def test_details_view_with_no_exist_id(self):
		pid = 1
		response = self.client.get(reverse('polls:details',args=(pid,)))
		self.assertEqual(response.status_code,404)	
	
	def test_details_view_with_a_future_poll(self):
		future_poll = create_poll(question='future poll.',days=5)
		response = self.client.get(reverse('polls:details',args=(future_poll.id,)))
		self.assertEqual(response.status_code,404)
	
	def test_details_view_with_a_past_poll(self):
		p = create_poll(question='past poll.',days=-30)
		response = self.client.get(reverse('polls:details',args=(p.id,)))
		self.assertContains(response,'past poll.')
