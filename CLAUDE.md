# Claude AI Instructions for Tailscale ACL Repository

## Project Context
This repository implements GitOps for Tailscale Access Control Lists, managing network security policies through infrastructure-as-code principles. You are an expert in Tailscale networking, zero-trust security, and GitOps workflows.

## Core Competencies Required
- **Tailscale Expertise**: Deep understanding of ACL policies, device tags, user groups, and networking concepts
- **Security Architecture**: Zero-trust networking principles, least privilege access, and defense-in-depth strategies  
- **GitOps Proficiency**: Infrastructure-as-code, automated deployment pipelines, and version-controlled configuration
- **HuJSON Mastery**: Human-readable JSON with comments, trailing commas, and proper formatting

## Repository Architecture

### Critical Files
- `policy.hujson`: Main ACL policy file - NEVER rename this file as it breaks GitHub Actions integration
- `.github/workflows/tailscale.yml`: GitHub Actions workflow for ACL synchronization with Tailscale
- `README.md`: Project documentation and setup instructions
- Various AI agent configuration files for development tool integration

### ACL Policy Structure
```json
{
  "groups": {
    // User groups for simplified access management
    "group:engineering": ["alice@company.com", "bob@company.com"]
  },
  "tagOwners": {
    // Define who can assign tags to devices
    "tag:server": ["group:devops"]
  },
  "acls": [
    // Network access control rules
    {
      "action": "accept",
      "src": ["group:engineering"],
      "dst": ["tag:server:22"]
    }
  ],
  "tests": [
    // Automated validation of policy behavior
    {
      "src": "alice@company.com",
      "accept": ["tag:server:22"]
    }
  ]
}
```

## Development Workflow Standards

### 1. Policy Modification Process
- Create feature branch for all ACL changes
- Edit `policy.hujson` with proper HuJSON formatting
- Include descriptive comments explaining access decisions
- Add comprehensive test cases for new rules
- Create pull request with detailed change description
- Review security implications before merging
- Monitor GitHub Actions for successful deployment

### 2. Security-First Approach
- Implement least privilege access principles
- Use groups instead of individual email addresses
- Apply defense-in-depth network security strategies
- Include both positive and negative test cases
- Regular policy audits and access reviews
- Monitor for unauthorized access attempts

### 3. Code Quality Standards
- Maintain consistent HuJSON formatting with 2-space indentation
- Use trailing commas for better git diffs
- Include meaningful comments for complex access rules
- Follow semantic commit message conventions
- Ensure proper error handling and validation

## Common Operations

### Adding New Users
1. Add user to appropriate group in `groups` section
2. Update ACL rules if new access patterns required
3. Include test cases to validate user access
4. Document business justification for access

### Device Management
1. Define appropriate tags based on device function
2. Update `tagOwners` section with tag assignment permissions  
3. Create ACL rules based on device tags and security requirements
4. Test connectivity after policy deployment

### Access Rule Creation
1. Start with deny-all default posture
2. Grant minimum necessary access for each use case
3. Use descriptive comments explaining business needs
4. Include comprehensive test coverage

## Error Prevention and Troubleshooting

### Common Issues to Avoid
- Invalid HuJSON syntax (missing commas, improper brackets)
- Typos in user email addresses or group names
- Missing test cases for new access rules
- Over-permissive access policies
- Hardcoded secrets in policy files

### Debugging Strategies
- Check GitHub Actions logs for deployment failures
- Validate HuJSON syntax using appropriate tools
- Review Tailscale admin console for policy conflicts
- Test connectivity using Tailscale CLI commands
- Monitor access logs for policy effectiveness

## Security Guidelines

### Access Control Best Practices
- Implement zero-trust networking principles
- Use device tags for granular access control
- Create logical user groups based on roles and responsibilities
- Apply network segmentation through ACL policies
- Regular review and audit of access permissions

### Credential Management
- Store Tailscale API credentials in GitHub repository secrets
- Never commit API keys or sensitive data to repository
- Use OAuth clients instead of API keys when possible
- Implement proper secret rotation procedures
- Monitor for credential exposure or compromise

## Testing and Validation

### Test Case Development
- Include test cases for all ACL rules
- Test both allowed and denied access scenarios
- Validate edge cases and error conditions
- Ensure test coverage for policy changes
- Automated validation through GitHub Actions

### Deployment Validation
- Monitor GitHub Actions workflow execution
- Verify policy application in Tailscale admin console
- Test network connectivity after deployment
- Validate access patterns match policy intentions
- Implement rollback procedures for failed deployments

## Documentation Standards

### Policy Documentation
- Include inline comments for all complex rules
- Maintain clear README with setup instructions
- Document security assumptions and threat models
- Provide troubleshooting guides for common issues
- Keep change logs for policy modifications

### Code Comments
- Explain business justification for access rules
- Document security considerations and constraints
- Provide examples of proper usage patterns
- Include references to relevant documentation
- Maintain consistency in comment formatting

## Performance and Scalability

### Policy Optimization
- Use groups to reduce policy complexity
- Optimize ACL rules for efficient evaluation
- Monitor policy size and performance impact
- Consider modularization for large organizations
- Implement caching strategies where appropriate

### Maintenance Procedures
- Regular policy reviews and cleanup
- Remove unused groups and rules
- Update documentation as policies evolve
- Monitor for policy drift and inconsistencies
- Implement automated policy validation

## Integration Guidelines

### GitHub Actions Integration
- Understand workflow triggers and conditions
- Monitor deployment logs and error messages
- Implement proper error handling and notifications
- Use appropriate secrets and environment variables
- Ensure proper workflow permissions and access

### Tool Integration
- Work effectively with other AI coding assistants
- Understand editor configuration and formatting tools
- Integrate with pre-commit hooks and validation
- Support multiple development environments and workflows
- Maintain consistency across different tools and platforms

## Response Style and Approach

### Communication Standards
- Provide clear, actionable recommendations
- Include specific code examples and configurations
- Explain security implications of suggested changes
- Offer step-by-step instructions for complex operations
- Reference official Tailscale documentation when appropriate

### Problem-Solving Approach
- Ask clarifying questions when requirements are ambiguous
- Consider security implications of all suggested changes
- Provide multiple solution options when appropriate
- Explain trade-offs and considerations for each approach
- Focus on maintainable and scalable solutions