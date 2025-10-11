# Create a comprehensive structure for all the AI coding agent configuration files
import json
import yaml
import os

# Create the main configuration files structure
configs = {
    ".cursorrules": """# Cursor IDE Rules for Tailscale ACL Repository

You are an expert DevOps engineer specializing in Tailscale network management, GitOps workflows, and infrastructure automation.

## Project Context
This repository manages Tailscale Access Control Lists (ACLs) through GitOps methodology, automatically syncing ACL policies to the Tailscale tailnet via GitHub Actions.

## Core Principles
- Always validate ACL syntax before making changes
- Follow GitOps principles - all changes through pull requests
- Maintain security-first approach to access control policies
- Use descriptive commit messages for ACL changes
- Test ACL changes in non-production environments first

## File Types and Standards
- `policy.hujson`: Main Tailscale ACL policy file (Human JSON format)
- `.github/workflows/tailscale.yml`: GitHub Actions workflow for ACL sync
- Documentation files: Use clear, concise Markdown
- Configuration files: Follow YAML best practices

## Tailscale ACL Guidelines
- Use groups for user management instead of individual email addresses
- Implement least privilege access principles  
- Tag devices appropriately for granular control
- Include comments explaining complex access rules
- Test ACL policies before production deployment

## Code Style
- HuJSON: Use human-readable formatting with comments
- YAML: 2-space indentation, no tabs
- Markdown: Use consistent heading structure
- JSON: Pretty-print with 2-space indentation

## Security Considerations
- Never commit API keys or secrets to the repository
- Use GitHub secrets for sensitive Tailscale credentials
- Regularly audit and review access control policies
- Document security assumptions and threat model

## Development Workflow
1. Create feature branch for ACL changes
2. Make changes to policy.hujson
3. Test changes locally if possible
4. Create pull request with detailed description
5. Review and approve before merging to main
6. Monitor GitHub Actions deployment

## Testing
- Use Tailscale's built-in ACL test functionality
- Include test cases in the policy file
- Verify connectivity after ACL deployments
- Test edge cases and error scenarios

## Error Handling
- Check GitHub Actions logs for deployment issues
- Validate HuJSON syntax before committing
- Handle API rate limits gracefully
- Provide clear error messages in documentation""",

    ".clinerules": """# Cline Rules for Tailscale ACL Management

## Project Overview
This repository manages Tailscale Access Control Lists using GitOps principles. The primary focus is on network security, infrastructure automation, and reliable ACL deployments.

## Key Technologies
- Tailscale: Zero-trust network access platform
- GitHub Actions: CI/CD for ACL synchronization  
- HuJSON: Human-readable JSON format for ACL policies
- GitOps: Infrastructure-as-code methodology

## Development Guidelines

### ACL Policy Management
- Edit only the policy.hujson file for ACL changes
- Use descriptive comments to explain access rules
- Follow least privilege security principles
- Group users logically using Tailscale groups
- Tag devices appropriately for access control

### File Structure
- `policy.hujson`: Main Tailscale ACL policy (do not rename)
- `.github/workflows/tailscale.yml`: GitHub Actions workflow
- `README.md`: Project documentation and setup instructions
- Configuration files: Various AI agent configurations

### Security Best Practices
- Never commit Tailscale API keys or secrets
- Use GitHub repository secrets for credentials
- Regularly audit access control policies
- Test ACL changes in staging environments
- Monitor failed deployments and access denials

### Testing Strategy
- Include ACL tests in the policy.hujson file
- Use Tailscale's built-in test functionality
- Validate connectivity after policy changes
- Test both positive and negative access scenarios

### Git Workflow
- Use feature branches for all ACL modifications
- Write descriptive commit messages explaining changes
- Require pull request reviews for policy changes
- Merge only after successful CI/CD validation

### Error Resolution
- Check GitHub Actions logs for deployment failures
- Validate HuJSON syntax using appropriate tools
- Monitor Tailscale admin console for policy conflicts
- Document and share solutions to common issues

## Common Commands
- Test ACL locally: Use Tailscale CLI tools where possible
- Validate HuJSON: Check syntax before committing
- Deploy policies: Automatic via GitHub Actions on merge
- Rollback: Use git revert for problematic changes

## Important Notes
- The repository syncs automatically to Tailscale on main branch changes
- Failed deployments will not update the Tailscale ACL policies
- Always test changes thoroughly before production deployment
- Keep the policy.hujson file as the single source of truth""",

    "COPILOT-FILES-SUMMARY.md": """# Copilot Files Summary for Tailscale ACL Repository

## Repository Purpose
This repository manages Tailscale Access Control Lists through GitOps workflows, providing infrastructure-as-code for network access policies.

## Key Files

### Core ACL Management
- `policy.hujson` - Main Tailscale ACL policy file in Human JSON format
- `.github/workflows/tailscale.yml` - GitHub Actions workflow for ACL synchronization
- `README.md` - Project documentation and setup instructions

### CI/CD Configuration  
- `.github/workflows/tailscale.yml` - Automated ACL deployment pipeline
- GitHub repository secrets for Tailscale API credentials

### Development Tools
- `.cursorrules` - Cursor IDE configuration for Tailscale ACL development
- `.clinerules` - Cline agent configuration and guidelines
- `AGENTS.md` - General AI agent instructions
- `.aider.conf.yml` - Aider configuration for ACL management

### Code Quality
- `.yamllint` - YAML linting configuration
- `.prettierrc` - Code formatting rules
- `.pre-commit-config.yaml` - Pre-commit hooks for validation
- `.editorconfig` - Editor configuration for consistency
- `.gitignore` / `.dockerignore` - Ignore files for clean repository

## Important Concepts

### Tailscale ACL Structure
- Groups: Named collections of users for access management
- Tags: Device categorization for granular access control
- ACLs: Network-level access control rules
- Tests: Validation of ACL policy correctness

### GitOps Workflow
1. Modify `policy.hujson` in feature branch
2. Create pull request with detailed change description
3. Review and approve changes
4. Merge triggers automatic deployment to Tailscale
5. Monitor deployment success in GitHub Actions

### Security Considerations
- All access changes go through code review process
- API credentials stored securely in GitHub secrets
- Failed deployments do not update production ACLs
- Regular policy auditing and validation

## Development Patterns
- Use descriptive group names and comments in ACL policies
- Implement least privilege access principles
- Include comprehensive test cases for ACL rules
- Follow consistent naming conventions for devices and users
- Document security assumptions and access requirements""",

    ".github/copilot_chat_instructions.md": """# GitHub Copilot Chat Instructions for Tailscale ACL Repository

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
- Compliance with organizational access policies""",

    "copilot_instructions_tailscale.md": """# Tailscale ACL Management Instructions for GitHub Copilot

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
- Monitoring and alerting for access control failures""",

    "AGENTS.md": """# AI Agent Instructions for Tailscale ACL Repository

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
- Keep policies simple and well-documented for maintainability""",

    "GEMINI_RULES.md": """# Gemini AI Rules for Tailscale ACL Repository

## Project Context and Role
You are a DevOps and network security expert specializing in Tailscale zero-trust networking and GitOps infrastructure management. This repository manages Tailscale Access Control Lists through automated GitOps workflows.

## Core Responsibilities
- Maintain secure, reliable network access policies
- Implement infrastructure-as-code principles for network security
- Ensure proper GitOps workflow adherence
- Optimize Tailscale ACL policies for security and performance

## Tailscale ACL Expertise

### ACL Policy Structure Understanding
- **Groups**: User collections for simplified access management
- **TagOwners**: Device tag assignment permissions  
- **ACLs**: Network access rules with source/destination matching
- **SSH**: Tailscale SSH access policies and configurations
- **Tests**: Automated policy validation and correctness verification

### HuJSON Format Mastery
- Use human-readable JSON with comments and trailing commas
- Maintain consistent indentation and formatting
- Include descriptive inline comments for complex rules
- Structure policies with logical section organization

### Security-First Approach
- Always apply least privilege access principles
- Use groups instead of individual email addresses when possible
- Implement defense-in-depth network security strategies
- Regular policy auditing and access pattern reviews

## Development Standards

### Code Quality
- Validate HuJSON syntax before committing changes
- Use descriptive naming conventions for groups and tags
- Include comprehensive test cases for all access rules
- Maintain clean, well-documented policy files

### Git Workflow Excellence
- Create feature branches for all policy modifications
- Write clear, semantic commit messages
- Require pull request reviews for policy changes
- Use git history for policy change tracking and rollbacks

### CI/CD Integration
- Understand GitHub Actions workflow for ACL deployment
- Monitor deployment success/failure in Actions logs  
- Implement proper secret management for Tailscale credentials
- Ensure testing before production policy deployment

## Common Tasks and Best Practices

### User Management
1. Add users to appropriate groups rather than individual ACL entries
2. Create logical group structures based on roles and responsibilities
3. Include test cases when adding new user access patterns
4. Document group purposes and membership criteria

### Device Tag Management  
1. Define clear tagging strategies for different device types
2. Assign tag ownership to appropriate user groups
3. Use tags for granular access control based on device function
4. Maintain tag documentation and usage guidelines

### Access Rule Creation
1. Start with deny-all default security posture
2. Grant minimum necessary access for each use case
3. Use descriptive comments explaining business justification
4. Include both positive and negative test cases

### Policy Testing and Validation
1. Include comprehensive test suites in policy files
2. Test edge cases and error scenarios
3. Validate connectivity after policy deployments
4. Monitor access patterns for policy effectiveness

## Error Prevention and Troubleshooting

### Common Pitfalls
- Syntax errors in HuJSON format
- Typos in user email addresses or group names
- Missing test cases for new access rules
- Insufficient access restrictions (over-permissive policies)

### Debugging Strategies
- Check GitHub Actions logs for deployment failures
- Validate policy syntax using appropriate tools
- Review Tailscale admin console for policy conflicts
- Test connectivity using Tailscale CLI tools

## Security Guidelines
- Never commit Tailscale API keys or secrets to repository
- Use GitHub repository secrets for sensitive credentials
- Implement regular policy reviews and access audits
- Monitor for unauthorized access attempts and policy violations
- Maintain audit trails for all policy changes

## Performance and Scalability
- Optimize ACL rules for efficient policy evaluation
- Use groups to reduce policy complexity and maintenance overhead
- Monitor policy size and complexity for scalability
- Consider policy modularization for large organizations

## Documentation Standards
- Maintain clear README with setup and usage instructions
- Include inline comments for all complex access rules
- Document security assumptions and threat model considerations
- Provide troubleshooting guides for common issues

## Response Style
- Provide concrete, actionable recommendations
- Include code examples for Tailscale ACL configurations
- Explain security implications of suggested changes
- Offer step-by-step instructions for complex operations
- Reference official Tailscale documentation when appropriate""",

    "README-COPILOT-SETUP.md": """# GitHub Copilot Setup for Tailscale ACL Repository

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
- Scalable policy structures for organizational growth""",

    "CLAUDE.md": """# Claude AI Instructions for Tailscale ACL Repository

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
- Focus on maintainable and scalable solutions""",

    ".aider.conf.yml": """# Aider Configuration for Tailscale ACL Repository

# Main model configuration
model: gpt-4o

# Repository-specific settings
read:
  - policy.hujson
  - README.md
  - .github/workflows/tailscale.yml
  - AGENTS.md

# Enable specific features for Tailscale ACL development
lint-cmd: yamllint .github/workflows/tailscale.yml
test-cmd: echo "No automated tests configured - manual validation required"
auto-commits: false
dirty-commits: true
commit-prompt: |
  Please provide a clear, semantic commit message that explains:
  1. The type of change (feat, fix, docs, refactor, etc.)
  2. What ACL policy changes were made
  3. The business justification or security impact
  4. Any testing performed

# File editing preferences
editor-edit-format: whole
edit-format: diff

# Git settings
git: true
gitignore: true
check-update: false

# Output and formatting
pretty: true
stream: true
user-input-color: "#00ff00"
tool-output-color: "#0088ff"
tool-error-color: "#ff0000"

# Tailscale-specific instructions
additional-instructions: |
  You are an expert in Tailscale ACL management and GitOps workflows. When working on this repository:
  
  1. NEVER rename the policy.hujson file - this breaks GitHub Actions integration
  2. Always maintain valid HuJSON format with comments and trailing commas
  3. Use groups for user management instead of individual email addresses
  4. Include comprehensive test cases for all ACL rule changes
  5. Follow least privilege security principles
  6. Add descriptive comments explaining the business reason for access rules
  7. Consider the security implications of all changes
  8. Validate that GitHub Actions workflow remains functional
  9. Include both positive and negative test scenarios
  10. Use semantic commit messages for better change tracking

# Environment variables (do not store secrets here)
env:
  TAILSCALE_REPO: "true"
  ACL_VALIDATION: "strict"

# Suggested commit message template
commit-message-template: |
  {type}: {description}
  
  {body}
  
  - Changed: {changed_files}
  - Security impact: {security_impact}
  - Testing: {testing_performed}""",

    ".vscode/settings.json": """{
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "editor.detectIndentation": false,
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,
  "editor.codeActionsOnSave": {
    "source.fixAll": true,
    "source.organizeImports": true
  },
  
  "files.associations": {
    "*.hujson": "jsonc",
    "policy.hujson": "jsonc",
    ".cursorrules": "markdown",
    ".clinerules": "markdown",
    "AGENTS.md": "markdown",
    "CLAUDE.md": "markdown",
    "GEMINI_RULES.md": "markdown"
  },
  
  "files.exclude": {
    ".git": true,
    "node_modules": true,
    ".DS_Store": true,
    "Thumbs.db": true
  },
  
  "json.validate.enable": true,
  "json.format.enable": true,
  "jsonc.format.enable": true,
  
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true
  },
  
  "[jsonc]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true,
    "editor.tabSize": 2
  },
  
  "[yaml]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true,
    "editor.tabSize": 2,
    "editor.autoIndent": "advanced"
  },
  
  "[markdown]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.wordWrap": "on",
    "editor.formatOnSave": true
  },
  
  "yaml.validate": true,
  "yaml.hover": true,
  "yaml.completion": true,
  "yaml.format.enable": true,
  "yaml.schemas": {
    "https://json.schemastore.org/github-workflow.json": ".github/workflows/*.yml"
  },
  
  "git.enableCommitSigning": false,
  "git.autofetch": true,
  "git.confirmSync": false,
  
  "tailscale-acl.enableLinting": true,
  "tailscale-acl.validateSyntax": true,
  
  "workbench.editor.enablePreview": false,
  "workbench.startupEditor": "readme",
  
  "terminal.integrated.defaultProfile.osx": "zsh",
  "terminal.integrated.defaultProfile.linux": "bash",
  "terminal.integrated.defaultProfile.windows": "PowerShell",
  
  "extensions.ignoreRecommendations": false,
  "extensions.showRecommendationsOnlyOnDemand": false
}""",

    ".gitignore": """# Operating System Files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Editor and IDE Files
.vscode/launch.json
.vscode/tasks.json
.idea/
*.swp
*.swo
*~
.project
.settings/

# Temporary Files
*.tmp
*.temp
*.log
*.pid
*.seed
*.lock

# Environment and Configuration
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
*.local

# Security Sensitive Files
*.key
*.pem
*.p12
*.crt
secrets.yaml
secrets.yml
config.secret.*

# Backup Files
*.bak
*.backup
*~

# Package Manager Files
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
package-lock.json
yarn.lock

# Build and Distribution
dist/
build/
out/
target/

# Cache and Runtime
.cache/
.npm
.eslintcache
.stylelintcache

# Test Coverage
coverage/
*.lcov
.nyc_output

# Logs
logs/
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Runtime Data
pids/
*.pid
*.seed
*.pid.lock

# Optional npm cache directory
.npm

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Docker
.dockerignore
Dockerfile.local

# Local development files
.local/
local.config.*
development.config.*

# AI and Editor Specific
.cursor/
.claude/
.aider*
.cline*

# OS generated files
.fseventsd
.DocumentRevisions-V100
.TemporaryItems
.VolumeIcon.icns
.AppleDouble
.LSOverride

# Network folders
Network Trash Folder
Temporary Items
.apdisk""",

    ".dockerignore": """.git
.gitignore
.github
.vscode
.idea

# Documentation
README.md
*.md
docs/
CHANGELOG.md
LICENSE
CONTRIBUTING.md

# Configuration files for development
.env*
.local
local.config.*
development.config.*

# Editor and IDE files
.DS_Store
Thumbs.db
*.swp
*.swo
*~

# Logs and temporary files
*.log
*.tmp
*.temp
logs/
temp/

# Test files and coverage
test/
tests/
spec/
coverage/
*.test.*
*.spec.*

# Development dependencies
node_modules/
.npm
.cache

# Build artifacts
dist/
build/
target/
out/

# CI/CD files (keep only necessary ones)
.github/workflows/
.travis.yml
.circleci/
.gitlab-ci.yml
azure-pipelines.yml

# Package manager files
package-lock.json
yarn.lock
composer.lock
Gemfile.lock

# Runtime and cache
.cache/
.eslintcache
.stylelintcache
.nyc_output

# Security sensitive files
*.key
*.pem
*.p12
*.crt
secrets.*

# Backup and temporary
*.bak
*.backup
*~

# AI agent configuration files (not needed in container)
.cursorrules
.clinerules
AGENTS.md
CLAUDE.md
GEMINI_RULES.md
.aider.conf.yml

# OS specific
.fseventsd
.DocumentRevisions-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.AppleDouble
.LSOverride
Network Trash Folder
Temporary Items
.apdisk""",

    ".yamllint": """---
extends: default

rules:
  line-length:
    max: 120
    level: warning
  
  indentation:
    spaces: 2
    indent-sequences: true
    check-multi-line-strings: false
  
  brackets:
    min-spaces-inside: 0
    max-spaces-inside: 1
    min-spaces-inside-empty: 0
    max-spaces-inside-empty: 0
  
  braces:
    min-spaces-inside: 0
    max-spaces-inside: 1
    min-spaces-inside-empty: 0
    max-spaces-inside-empty: 0
  
  colons:
    max-spaces-before: 0
    max-spaces-after: 1
  
  commas:
    max-spaces-before: 0
    min-spaces-after: 1
    max-spaces-after: 1
  
  comments:
    min-spaces-from-content: 1
    require-starting-space: true
  
  comments-indentation: {}
  
  document-end: disable
  document-start: disable
  
  empty-lines:
    max: 2
    max-start: 0
    max-end: 1
  
  empty-values:
    forbid-in-block-mappings: true
    forbid-in-flow-mappings: true
  
  hyphens:
    max-spaces-after: 1
  
  key-duplicates: {}
  key-ordering: disable
  
  new-line-at-end-of-file: {}
  octal-values: {}
  quoted-strings: disable
  trailing-spaces: {}
  truthy:
    allowed-values: ['true', 'false', 'yes', 'no']

# Ignore certain files and patterns
ignore: |
  .github/workflows/
  node_modules/
  .git/
  *.json
  *.hujson""",

    ".prettierrc": """{
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "semi": true,
  "singleQuote": true,
  "quoteProps": "as-needed",
  "trailingComma": "es5",
  "bracketSpacing": true,
  "bracketSameLine": false,
  "arrowParens": "avoid",
  "endOfLine": "lf",
  "embeddedLanguageFormatting": "auto",
  
  "overrides": [
    {
      "files": ["*.json", "*.jsonc"],
      "options": {
        "printWidth": 80,
        "tabWidth": 2,
        "trailingComma": "none"
      }
    },
    {
      "files": ["*.hujson", "policy.hujson"],
      "options": {
        "parser": "json",
        "printWidth": 100,
        "tabWidth": 2,
        "trailingComma": "all"
      }
    },
    {
      "files": ["*.yaml", "*.yml"],
      "options": {
        "printWidth": 120,
        "tabWidth": 2,
        "singleQuote": false
      }
    },
    {
      "files": ["*.md", "*.markdown"],
      "options": {
        "printWidth": 80,
        "proseWrap": "preserve",
        "tabWidth": 2
      }
    },
    {
      "files": [".cursorrules", ".clinerules", "AGENTS.md", "CLAUDE.md"],
      "options": {
        "parser": "markdown",
        "printWidth": 100,
        "proseWrap": "preserve"
      }
    }
  ]
}""",

    ".pre-commit-config.yaml": """---
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
        args: ['--unsafe']
      - id: check-json
      - id: check-added-large-files
        args: ['--maxkb=1000']
      - id: check-case-conflict
      - id: check-merge-conflict
      - id: debug-statements
      - id: detect-private-key

  - repo: https://github.com/adrienverge/yamllint
    rev: v1.32.0
    hooks:
      - id: yamllint
        args: [--format, parsable, --strict]
        exclude: ^(.github/workflows/|node_modules/)

  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v3.0.0
    hooks:
      - id: prettier
        exclude: ^(policy\.hujson|\.cursorrules|\.clinerules)$

  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/PyCQA/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/shellcheck-py/shellcheck-py
    rev: v0.9.0.5
    hooks:
      - id: shellcheck

  - repo: https://github.com/Lucas-C/pre-commit-hooks-safety
    rev: v1.3.2
    hooks:
      - id: python-safety-dependencies-check

  - repo: local
    hooks:
      - id: hujson-syntax-check
        name: Validate HuJSON syntax for Tailscale policy
        entry: bash
        language: system
        files: '^policy\.hujson$'
        args:
          - -c
          - |
            if command -v jq >/dev/null 2>&1; then
              # Use jq to validate JSON syntax, ignoring comments
              cat policy.hujson | sed 's|//.*||g' | jq . >/dev/null
              echo "HuJSON syntax validation passed for policy.hujson"
            else
              echo "Warning: jq not available for HuJSON validation"
            fi

      - id: tailscale-acl-security-check
        name: Basic security checks for Tailscale ACL
        entry: bash
        language: system
        files: '^policy\.hujson$'
        args:
          - -c
          - |
            echo "Running basic security checks on Tailscale ACL policy..."
            
            # Check for overly permissive rules
            if grep -q '"action": "accept".*"*"' policy.hujson; then
              echo "Warning: Found potentially overly permissive ACL rules using wildcards"
            fi
            
            # Check for individual email addresses (should use groups)
            if grep -oE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' policy.hujson | wc -l > 5; then
              echo "Warning: Consider using groups instead of individual email addresses"
            fi
            
            # Check for test cases
            if ! grep -q '"tests":' policy.hujson; then
              echo "Warning: No test cases found in policy.hujson"
              exit 1
            fi
            
            echo "Basic security checks completed"

      - id: no-secrets-check
        name: Check for potential secrets in files
        entry: bash
        language: system
        exclude: ^(.git/|node_modules/)
        args:
          - -c
          - |
            if grep -r -E "(api[_-]?key|secret|token|password|pwd)" --include="*.json" --include="*.yaml" --include="*.yml" --include="*.md" .; then
              echo "Warning: Potential secrets found in files"
              exit 1
            fi

# Global pre-commit configuration
default_stages: [commit]
fail_fast: false
minimum_pre_commit_version: 3.0.0""",

    ".eslintrc.js": """module.exports = {
  env: {
    node: true,
    es2022: true,
  },
  extends: [
    'eslint:recommended',
    'prettier',
  ],
  parserOptions: {
    ecmaVersion: 2022,
    sourceType: 'module',
  },
  rules: {
    // Security rules for configuration files
    'no-console': 'warn',
    'no-debugger': 'error',
    'no-eval': 'error',
    'no-implied-eval': 'error',
    'no-script-url': 'error',
    
    // Best practices
    'eqeqeq': 'error',
    'no-var': 'error',
    'prefer-const': 'error',
    'prefer-arrow-callback': 'error',
    
    // Formatting (handled by Prettier, but keeping some ESLint rules)
    'quotes': ['error', 'single', { avoidEscape: true }],
    'semi': ['error', 'always'],
    
    // Tailscale-specific rules for configuration management
    'no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
    'no-undef': 'error',
  },
  
  overrides: [
    {
      files: ['*.json', '*.jsonc'],
      parser: '@eslint/json',
      rules: {
        // JSON-specific rules for policy.hujson and other config files
        'json/no-duplicate-keys': 'error',
      },
    },
  ],
  
  ignorePatterns: [
    'node_modules/',
    '.git/',
    'dist/',
    'build/',
    '*.min.js',
    '.github/workflows/', // GitHub Actions files use different validation
  ],
};""",

    ".editorconfig": """# EditorConfig is awesome: https://EditorConfig.org

# top-most EditorConfig file
root = true

# All files
[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
indent_style = space
indent_size = 2

# Markdown files
[*.md]
max_line_length = 100
trim_trailing_whitespace = false

# JSON and HuJSON files (including Tailscale policy)
[*.{json,jsonc,hujson}]
indent_size = 2
insert_final_newline = true
max_line_length = 120

# YAML files (including GitHub Actions workflows)
[*.{yml,yaml}]
indent_size = 2
max_line_length = 120

# Shell scripts
[*.{sh,bash,zsh}]
indent_size = 2
max_line_length = 120

# Python files
[*.py]
indent_size = 4
max_line_length = 88

# Makefiles
[Makefile]
indent_style = tab
indent_size = 4

# Configuration files
[.{cursorrules,clinerules}]
indent_size = 2
max_line_length = 100

# AI agent instruction files
[{AGENTS,CLAUDE,GEMINI_RULES}.md]
indent_size = 2
max_line_length = 100
trim_trailing_whitespace = false

# Docker files
[{Dockerfile,Dockerfile.*}]
indent_size = 2

# Git configuration
[.git{ignore,attributes}]
indent_size = 2

# License and readme files
[{LICENSE,README,CHANGELOG,CONTRIBUTING}*]
max_line_length = 100
trim_trailing_whitespace = false""",
}

# Create directory structure and files
directories_to_create = [
    ".github", ".vscode", ".cursor"
]

for directory in directories_to_create:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Write all configuration files
for filename, content in configs.items():
    if "/" in filename:
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    with open(filename, 'w') as f:
        f.write(content)

print("Created all AI coding agent configuration files:")
for filename in configs.keys():
    print(f"  ✓ {filename}")

print("\nFiles created successfully! Summary:")
print(f"  • Total files: {len(configs)}")
print(f"  • AI agent configs: 8")
print(f"  • Development tools: 6") 
print(f"  • Quality/linting: 4")
print(f"  • Documentation: 2")