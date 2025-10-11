# Tailscale ACL Management Instructions for GitHub Copilot

## Repository Overview
This repository implements GitOps for Tailscale Access Control Lists, providing version-controlled network access policy management with automated deployment.

## Core Technologies and Concepts

### Tailscale
- Zero-trust network access platform
- Device-centric security model with dynamic key exchange
- Support for subnet routers, exit nodes, and app connectors
- HuJSON-based policy configuration

### ACL Policy Structure
- **Groups**: Collections of users for simplified management
- **TagOwners**: Define who can apply tags to devices  
- **ACLs**: Network access rules based on source/destination
- **SSH**: Tailscale SSH access policies
- **Tests**: Automated validation of policy behavior

### GitOps Workflow
- Policy changes via pull requests
- Automated validation on PR creation
- Automatic deployment to Tailscale on main branch merge
- Rollback capabilities through git history

## Development Best Practices

### Policy File Management
- Maintain policy.hujson as single source of truth
- Use descriptive comments for complex access rules
- Implement consistent naming conventions
- Structure policies with logical grouping

### Security Guidelines
- Apply least privilege access principles
- Use groups instead of individual email addresses
- Tag devices based on function and security requirements
- Regular policy auditing and access reviews

### Testing Strategy
- Include comprehensive test cases in policy file
- Test both positive and negative access scenarios
- Validate policy changes before production deployment
- Monitor access patterns and policy effectiveness

### Git Workflow
- Create feature branches for all policy changes
- Write clear commit messages describing access changes
- Require code review for all policy modifications
- Use semantic commit messages for better tracking

## Common Operations

### Adding New Users
1. Add user to appropriate groups in policy.hujson
2. Update ACL rules if new access patterns needed
3. Include tests to validate user access
4. Document changes in pull request

### Device Management
1. Define appropriate tags for device categories
2. Update tagOwners section for tag assignment permissions
3. Create ACL rules based on device tags and functions
4. Test connectivity for new device categories

### Troubleshooting Access Issues
1. Review ACL rules for source/destination matches
2. Check group membership and tag assignments
3. Validate policy syntax and structure
4. Monitor GitHub Actions logs for deployment issues

## File-Specific Guidelines

### policy.hujson
- Primary ACL policy configuration
- Must be valid HuJSON (JSON with comments and trailing commas)
- Include comprehensive comments explaining access decisions
- Structure with clear sections and consistent formatting

### .github/workflows/tailscale.yml
- GitHub Actions workflow for ACL synchronization
- Uses official Tailscale GitOps action
- Requires proper secret configuration
- Handles both testing (PR) and deployment (main) scenarios

### Documentation Files
- README.md: Setup and usage instructions
- This file: Copilot-specific guidance
- Inline comments in policy file for complex rules

## Error Handling
- Syntax validation prevents invalid policy deployment
- Failed GitHub Actions runs prevent policy updates
- Git history enables quick rollback of problematic changes
- Monitoring and alerting for access control failures