# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.
- VM: B1s(free services eligible)
  - Cost: estimate $9.64/month
  - Scalability: Yes
  - Availability: Multi region support
  - Workflow: manual, we need to setup how to make application up and running, also expose to the public internet
- App Service Plan: B1
  - Cost: Estimate $13.14/month
  - Scalability: can easy scale up/Scale out
  - Availability: Multi region support
  - Workflow: select runtime stack and easy connect with Github to deploy Flask application
- I choose App Service Plan because it's compatible cost and easy to deploy
### Assess app changes that would change your decision.
- If the application grow, perhaps the cost of the app service more expensive than the cost of the VM. Then I will think to use VM insteads of App Service.
