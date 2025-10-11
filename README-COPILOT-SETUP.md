# GitHub Copilot Setup for Tailscale ACL Repository

## Overview
This document provides specific guidance for configuring GitHub Copilot to work effectively with Tailscale ACL management in this repository.

## Copilot Configuration Files

### Repository-Wide Instructions
The `.github/copilot_chat_instructions.md` file contains repository-wide instructions that Copilot automatically loads when working in this repository. These instructions provide:

- Context about Tailscale ACL management and GitOps workflows
- HuJSON formatting standards and best practices
- Security guidelines for network access policy development
- Common development patterns and tasks

### Project-Specific Instructions
The `copilot_instructions_tailscale.md` file contains detailed Tailscale-specific guidance including:

- Tailscale ACL policy structure and components
- GitOps workflow for ACL deployments
- Security best practices and testing strategies
- Common operations and troubleshooting guidance

## Copilot Best Practices for This Repository

### Understanding ACL Structure
When working with `policy.hujson`, Copilot should understand:
- HuJSON format allows comments and trailing commas
- Policy structure includes groups, tagOwners, acls, and tests sections
- Use descriptive names and include explanatory comments
- Follow least privilege security principles

### Security-First Development
Copilot should always:
- Recommend least privilege access patterns
- Suggest using groups instead of individual emails
- Include test cases for new access rules
- Validate security implications of changes

### GitOps Workflow Awareness
Copilot understands that:
- Changes to main branch automatically deploy to Tailscale
- Pull requests trigger validation without deployment
- Failed GitHub Actions prevent policy updates
- Git history enables policy rollbacks

## Common Copilot Use Cases

### 1. Adding New Users to Groups
```json
// Copilot can help add users to existing groups
"groups": {
  "group:engineering": [
    "alice@company.com",
    "bob@company.com",
    "newuser@company.com"  // Added by Copilot
  ]
}
```

### 2. Creating New Access Rules
```json
// Copilot can suggest proper ACL rule structure
{
  "action": "accept",
  "src": ["group:engineering"],
  "dst": ["tag:database:5432"],
  "comment": "Engineering team access to database servers"
}
```

### 3. Writing Test Cases
```json
// Copilot can generate comprehensive test cases
{
  "src": "alice@company.com",
  "accept": ["tag:server:22", "tag:server:80"],
  "deny": ["tag:server:3389"]
}
```

### 4. Documenting Policy Changes
Copilot can help write clear commit messages and pull request descriptions:
```
feat: add QA team access to staging environment

- Added group:qa with QA team members
- Created ACL rule for QA access to tag:staging servers on ports 22, 80, 443
- Included test cases for positive and negative access scenarios
- Updated tagOwners to allow QA team to manage staging tags
```

## HuJSON Formatting Guidelines

Copilot should follow these formatting standards:
- Use 2-space indentation consistently
- Include trailing commas for better git diffs
- Add descriptive comments for complex rules
- Maintain consistent bracket and brace alignment
- Use meaningful whitespace for readability

## Security Validation

Copilot should validate:
- No hardcoded secrets or API keys in policy files
- Proper use of groups instead of individual emails where possible
- Implementation of least privilege access principles
- Inclusion of appropriate test cases for access validation
- Clear comments explaining security decisions

## Error Prevention

Common issues Copilot should help avoid:
- Invalid HuJSON syntax (missing commas, brackets)
- Typos in email addresses and group names
- Missing or inadequate test cases
- Over-permissive access rules
- Insufficient documentation of policy changes

## Testing and Validation

Copilot should encourage:
- Including test cases for all new access rules
- Testing both allowed and denied access scenarios
- Validating policy syntax before committing
- Monitoring GitHub Actions for deployment success
- Reviewing Tailscale admin console for policy application

## Integration with Other Tools

Copilot works alongside:
- `.cursorrules` for Cursor IDE integration
- `.clinerules` for Cline agent configuration
- `AGENTS.md` for general AI agent guidance
- GitHub Actions for automated ACL deployment
- Pre-commit hooks for policy validation

## Troubleshooting with Copilot

When issues arise, Copilot can help:
- Identify syntax errors in HuJSON files
- Suggest fixes for failed GitHub Actions workflows  
- Debug access control policy issues
- Generate test cases to isolate problems
- Recommend security improvements

## Continuous Improvement

Copilot should help maintain:
- Regular policy reviews and audits
- Documentation updates as policies evolve
- Best practice adoption across the organization
- Knowledge sharing through clear code comments
- Scalable policy structures for organizational growth