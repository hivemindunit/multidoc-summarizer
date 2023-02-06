# MultiDoc Summarizer
API to reduce input phrases list utilizing the latent semantic analysis algorithm.  
- Input
  - documents: [String] - _list of phrases_
- Output
  - documents: [String] - _list of phrases after LSA_
### Input Sample
```json
{
  "documents": [
    "It was raining, therefore I stayed my office.", 
    "My printer got broken as a consequence of I borrowed my friend’s.",
    "Mark works not only careless but also hasty.",
    "All of my sisters are doctors, whereas I am a teacher.",
    "I want to call his, but I don’t have his phone number.",
    "Although she ran very fast, she lost the race.",
    "They didn’t go to the party, although they were invited.",
    "Though the weather was very cold and snowy, the kids played outside.",
    "She doesn’t want to go to the doctor ,though she is very sick.",
    "They met in order to get information from each other about the project.",
    "Let me know if you go to the school.",
    "Whoever says so is a liar.",
    "I go to work on Sundays, but I don’t go to work on Saturday.",
    "We couldn’t go to the park today, however, we had a lot of work, we couldn’t play games at home.",
    "You are important for me; nonetheless, sometimes I feel like you don’t even take care of me.",
    "Neither Mark nor Mary were at the school yesterday.",
    "The more you can dream, the more you can do.",
    "I would rather go out than stay at home today.",
    "Scarcely had I gone to bed when the doorbell rang.",
    "I will go to England in order to improve my English.",
    "She is not our best worker, but nevertheless she tries very hard.",
    "It’s raining very hard today. However, let’s go out and enjoy ourselves!",
    "In spite of the fog, planes are still landing.",
    "While I like pop music my husband hates it.",
    "In spite of all the cooking shows I’ve watched, I’m still no good in the kitchen.",
    "Although studying French seems difficult, it’s simpler than you think.",
    "She loved flowers, and I always bought her flowers, however she didn’t like to get them.",
    "As soon as Marry arrives in the room, I will start telling her what we are experiencing today.",
    "I would like to help you with this and ease your burden, yet unfortunately, I have no time.",
    "Would you rather go to the movie that we talked about last night or spend the day at home with Netflix?"
  ]
}
```
### Output Sample
```
[
  "It was raining, therefore I stayed my office.",
  "Mark works not only careless but also hasty.",
  "All of my sisters are doctors, whereas I am a teacher.",
  "They met in order to get information from each other about the project.",
  "Let me know if you go to the school.",
  "Neither Mark nor Mary were at the school yesterday.",
  "I would rather go out than stay at home today.",
  "Scarcely had I gone to bed when the doorbell rang.",
  "In spite of the fog, planes are still landing.",
  "While I like pop music my husband hates it.",
  "Although studying French seems difficult, it’s simpler than you think.",
  "Would you rather go to the movie that we talked about last night or spend the day at home with Netflix?"
]
```

## Tech Stack
- [Serverless](https://www.serverless.com/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Sumy](https://miso-belica.github.io/sumy/)
- [NLTK](https://www.nltk.org/)
## Deployment
### Set AWS Credentials 
Run `aws configure` and enter AWS credentials (Access Key ID and Secret Access Key).
### Create an ECR repository
This should be done only once, if the repository already exists, move on to the next step.
```shell
aws ecr create-repository --repository-name over-quota-multidoc-summarizer
```
### Build Docker Image
```shell
docker build -t over-quota-multidoc-summarizer .
```
### Authenticate Docker CLI with AWS ECR
```shell
aws ecr get-login-password | docker login --username AWS --password-stdin 070835681152.dkr.ecr.us-east-1.amazonaws.com
```
### Tag the Image with the Repository URI
```shell
docker tag over-quota-multidoc-summarizer 070835681152.dkr.ecr.us-east-1.amazonaws.com/over-quota-multidoc-summarizer
```
### Push the Image to ECR Repository
```shell
docker push 070835681152.dkr.ecr.us-east-1.amazonaws.com/over-quota-multidoc-summarizer
```
### Deploy Lambda Function
```shell
serverless deploy
```
