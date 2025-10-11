# AI Agent Instructions for Tailscale ACL Repository

## Project Overview
This repository manages Tailscale Access Control Lists through GitOps methodology, enabling infrastructure-as-code for network security policies. The primary goal is maintaining secure, reliable, and auditable network access control.

## Core Technologies
- **Tailscale**: Zero-trust network access platform with WireGuard-based mesh networking
- **GitOps**: Infrastructure management through Git workflows and automated deployment
- **HuJSON**: Human-readable JSON format for ACL policies with comments and trailing commas
- **GitHub Actions**: CI/CD pipeline for ACL validation and deployment

## Repository Structure

### Essential Files
- `policy.hujson`: Main Tailscale ACL policy file (NEVER rename this file)
- `.github/workflows/tailscale.yml`: GitHub Actions workflow for ACL synchronization
- `README.md`: Project documentation and setup instructions

### Configuration Files
- `.cursorrules`, `.clinerules`: AI agent-specific configurations
- `.yamllint`, `.prettierrc`: Code quality and formatting tools
- `.editorconfig`: Cross-editor consistency settings
- `.gitignore`: Git ignore patterns for clean repository

## Development Workflow

### 1. ACL Policy Changes
- Edit `policy.hujson` in feature branches only
- Use HuJSON format with comments and trailing commas
- Include test cases for all new access rules
- Follow least privilege security principles

### 2. Git Workflow
```bash
# Create feature branch
git checkout -b feature/add-user-group

# Make changes to policy.hujson
# Commit with descriptive messages
git commit -m "feat: add engineering team access to production servers"

# Push and create pull request
git push origin feature/add-user-group
```

### 3. CI/CD Process
- Pull requests trigger ACL validation (test action)
- Merging to main triggers deployment (apply action)
- Monitor GitHub Actions logs for deployment status
- Failed deployments prevent policy updates

## Tailscale ACL Best Practices

### Policy Structure
```json
{
  // Define user groups for easier management
  "groups": {
    "group:engineering": ["alice@company.com", "bob@company.com"],
    "group:devops": ["charlie@company.com"]
  },

  // Define who can assign tags to devices
  "tagOwners": {
    "tag:server": ["group:devops"],
    "tag:workstation": ["group:engineering", "group:devops"]
  },

  // Access control rules
  "acls": [
    {
      "action": "accept",
      "src": ["group:engineering"],
      "dst": ["tag:server:22", "tag:server:80", "tag:server:443"]
    }
  ],

  // Test cases to validate policy behavior
  "tests": [
    {
      "src": "alice@company.com",
      "accept": ["tag:server:22"],
      "deny": ["tag:server:3389"]
    }
  ]
}
```

### Security Guidelines
- Use groups instead of individual email addresses
- Tag devices based on function and security requirements
- Implement least privilege access (deny by default)
- Include comprehensive test cases
- Regular policy auditing and access reviews

### Naming Conventions
- Groups: `group:team-name` or `group:function`
- Tags: `tag:device-type` or `tag:environment`
- Comments: Explain the business reason for access rules

## Common Operations

### Adding New Users
1. Add users to appropriate groups in `groups` section
2. Update ACL rules if new access patterns are needed
3. Add test cases to validate user access
4. Document changes in pull request description

### Managing Device Access
1. Define appropriate tags for new device categories
2. Update `tagOwners` section with tag assignment permissions
3. Create ACL rules based on device tags and requirements
4. Test connectivity after policy deployment

### Troubleshooting
1. Check GitHub Actions logs for deployment failures
2. Validate HuJSON syntax and structure
3. Review ACL rules for source/destination matches
4. Monitor Tailscale admin console for policy conflicts

## Security Considerations
- All credentials stored in GitHub repository secrets
- Never commit API keys or passwords to repository
- Regular policy reviews and access audits
- Implement defense-in-depth access strategies
- Monitor for unauthorized access attempts

## Testing Strategy
- Include test cases for all ACL rules
- Test both positive (allowed) and negative (denied) scenarios
- Validate policy changes in staging environments when possible
- Automated validation via GitHub Actions

## Error Handling
- Syntax validation prevents deployment of invalid policies
- Failed GitHub Actions runs prevent policy updates
- Git history enables quick rollback of problematic changes
- Comprehensive logging for troubleshooting access issues

## Important Notes
- The `policy.hujson` file is the single source of truth
- Changes to main branch automatically deploy to Tailscale
- Pull requests allow testing without affecting production
- Keep policies simple and well-documented for maintainability