from scraper.user_agents import get_random_user_agent

for _ in range(5):
    print(get_random_user_agent())