# GitHub Copilot Chat Instructions for Tailscale ACL Repository

## Context
This repository manages Tailscale Access Control Lists using GitOps principles. The primary goal is secure, reliable network access policy management through infrastructure-as-code.

## Tailscale ACL Development Guidelines

### When modifying policy.hujson:
- Always include descriptive comments explaining access rules
- Use Tailscale groups instead of individual email addresses when possible
- Follow least privilege security principles
- Include test cases to validate ACL behavior
- Maintain consistent indentation and formatting

### HuJSON Format Standards:
- Use trailing commas for better git diffs
- Include inline comments for complex rules
- Structure policies with clear sections (groups, tagOwners, acls, tests)
- Use descriptive names for groups and tags

### GitHub Actions Integration:
- Understand that changes to main branch automatically deploy to Tailscale
- Pull requests trigger ACL validation without deployment
- Monitor workflow runs for deployment success/failure
- Use appropriate secrets for Tailscale API authentication

### Security Best Practices:
- Never hardcode API keys or secrets in policy files
- Implement defense-in-depth access strategies
- Regularly audit and review access policies
- Use device tags for granular access control
- Document security assumptions clearly

### Testing Approach:
- Include comprehensive test cases in the policy file
- Test both allowed and denied access scenarios
- Validate policies before merging to main branch
- Use staging environments when possible

### Common Tasks:
1. Adding new users to groups
2. Creating new access rules for services
3. Modifying device tag assignments
4. Updating ACL tests for policy changes
5. Troubleshooting access control issues

### Error Prevention:
- Validate HuJSON syntax before committing
- Check for typos in user emails and group names
- Ensure proper group membership before creating ACL rules
- Test connectivity after policy deployments
- Monitor for failed GitHub Actions workflows

## Code Review Focus Areas:
- Security implications of access changes
- Correctness of HuJSON syntax and structure
- Completeness of test coverage for new rules
- Documentation of policy changes and rationale
- Compliance with organizational access policies