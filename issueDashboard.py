from github import Github
# from cfig import GithubToken
from config import (
    IssueTableHead,
    IssueTableTemplate
)
import argparse

# import sys

parser = argparse.ArgumentParser()
parser.add_argument("github_token", help="github_token")
options = parser.parse_args()
GithubToken = options.github_token

GithubToken = sys.argv[1]
print(GithubToken)

# issueFileName = "index.md"

# g = Github(GithubToken)
# me = g.get_user().login

# repo = g.get_repo("bgzocg/2021")
# openIssues = repo.get_issues(state='open', sort='updated') # creator=me,


# with open(issueFileName, "w+") as f:
#     f.write( IssueTableHead )
#     for issue in openIssues:
#         issueName = str(issue.title)
#         issueUpdate = str(issue.updated_at)
#         issueUrl = '#'+ str(issue.number)

#         f.write( IssueTableTemplate.format(
#             issueName = issueName, 
#             issueUpdate = issueUpdate, 
#             issueUrl = issueUrl
#         ) )
