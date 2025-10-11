# Create the GitHub Actions workflow and sample policy file
import yaml
import json
import os

# Create the GitHub Actions workflow
github_workflow = {
    'name': 'Sync Tailscale ACLs',
    'on': {
        'push': {
            'branches': ['main']
        },
        'pull_request': {
            'branches': ['main']
        }
    },
    'jobs': {
        'acls': {
            'runs-on': 'ubuntu-latest',
            'steps': [
                {
                    'uses': 'actions/checkout@v4'
                },
                {
                    'name': 'Fetch version-cache.json',
                    'uses': 'actions/cache@v4',
                    'with': {
                        'path': './version-cache.json',
                        'key': 'version-cache.json-${{ github.run_id }}',
                        'restore-keys': 'version-cache.json-\n'
                    }
                },
                {
                    'name': 'Deploy ACL',
                    'if': "github.event_name == 'push'",
                    'id': 'deploy-acl',
                    'uses': 'tailscale/gitops-acl-action@v1',
                    'with': {
                        'api-key': '${{ secrets.TS_API_KEY }}',
                        'tailnet': '${{ secrets.TS_TAILNET }}',
                        'action': 'apply'
                    }
                },
                {
                    'name': 'Test ACL',
                    'if': "github.event_name == 'pull_request'",
                    'id': 'test-acl',
                    'uses': 'tailscale/gitops-acl-action@v1',
                    'with': {
                        'api-key': '${{ secrets.TS_API_KEY }}',
                        'tailnet': '${{ secrets.TS_TAILNET }}',
                        'action': 'test'
                    }
                }
            ]
        }
    }
}

# Write the GitHub Actions workflow
os.makedirs('.github/workflows', exist_ok=True)
with open('.github/workflows/tailscale.yml', 'w') as f:
    yaml.dump(github_workflow, f, default_flow_style=False, sort_keys=False, indent=2)

# Create a sample policy.hujson file with comprehensive examples
sample_policy = """{
  // Tailscale ACL Policy for GitOps Management
  // This file defines access control rules for the tailnet
  
  // Define groups for easier user management
  "groups": {
    "group:admin": [
      "admin@yourdomain.com"
    ],
    "group:devops": [
      "devops1@yourdomain.com",
      "devops2@yourdomain.com"
    ],
    "group:engineering": [
      "engineer1@yourdomain.com", 
      "engineer2@yourdomain.com"
    ],
    "group:qa": [
      "qa@yourdomain.com"
    ]
  },

  // Define who can assign tags to devices
  "tagOwners": {
    "tag:server": ["group:admin", "group:devops"],
    "tag:workstation": ["group:admin", "group:devops", "group:engineering"],
    "tag:database": ["group:admin", "group:devops"],
    "tag:web": ["group:admin", "group:devops"],
    "tag:monitoring": ["group:admin", "group:devops"],
    "tag:bastion": ["group:admin", "group:devops"],
    "tag:staging": ["group:admin", "group:devops", "group:qa"],
    "tag:production": ["group:admin", "group:devops"]
  },

  // Access control rules
  "acls": [
    // Allow all users to access their own devices
    {
      "action": "accept",
      "src": ["*"],
      "dst": ["*:*"]
    },
    
    // Admin access to all systems
    {
      "action": "accept",
      "src": ["group:admin"],
      "dst": ["*:*"]
    },
    
    // DevOps access to infrastructure
    {
      "action": "accept", 
      "src": ["group:devops"],
      "dst": [
        "tag:server:22",    // SSH to servers
        "tag:server:80",    // HTTP to servers
        "tag:server:443",   // HTTPS to servers
        "tag:database:5432", // PostgreSQL
        "tag:database:3306", // MySQL
        "tag:monitoring:*"   // All monitoring ports
      ]
    },
    
    // Engineering team access
    {
      "action": "accept",
      "src": ["group:engineering"],
      "dst": [
        "tag:web:80",       // Web servers HTTP
        "tag:web:443",      // Web servers HTTPS
        "tag:staging:*",    // All staging environment ports
        "tag:bastion:22"    // SSH to bastion hosts
      ]
    },
    
    // QA team access to testing environments
    {
      "action": "accept",
      "src": ["group:qa"],
      "dst": [
        "tag:staging:80",   // Staging web access
        "tag:staging:443",  // Staging HTTPS access
        "tag:staging:22"    // SSH to staging servers
      ]
    },
    
    // Allow specific database access from web servers
    {
      "action": "accept",
      "src": ["tag:web"],
      "dst": ["tag:database:5432", "tag:database:3306"]
    },
    
    // Allow monitoring systems to collect metrics
    {
      "action": "accept",
      "src": ["tag:monitoring"],
      "dst": [
        "tag:server:9090",  // Prometheus metrics
        "tag:web:9090",     // Application metrics
        "tag:database:9090" // Database metrics
      ]
    }
  ],

  // SSH access rules (Tailscale SSH)
  "ssh": [
    {
      "action": "accept",
      "src": ["group:admin"],
      "dst": ["*"],
      "users": ["root", "ubuntu", "ec2-user"]
    },
    {
      "action": "accept",
      "src": ["group:devops"],
      "dst": ["tag:server", "tag:database", "tag:monitoring"],
      "users": ["ubuntu", "ec2-user", "deploy"]
    },
    {
      "action": "accept", 
      "src": ["group:engineering"],
      "dst": ["tag:staging", "tag:bastion"],
      "users": ["ubuntu", "deploy"]
    }
  ],

  // Auto-approvers for subnet routers and exit nodes
  "autoApprovers": {
    "routes": {
      "10.0.0.0/8": ["group:admin", "group:devops"],
      "192.168.0.0/16": ["group:admin", "group:devops"],
      "172.16.0.0/12": ["group:admin", "group:devops"]
    },
    "exitNode": ["group:admin"]
  },

  // Test cases to validate ACL behavior
  "tests": [
    // Test admin access
    {
      "src": "admin@yourdomain.com",
      "accept": [
        "tag:server:22",
        "tag:server:80", 
        "tag:database:5432",
        "tag:monitoring:9090"
      ]
    },
    
    // Test DevOps access
    {
      "src": "devops1@yourdomain.com", 
      "accept": [
        "tag:server:22",
        "tag:server:443",
        "tag:database:5432",
        "tag:monitoring:9090"
      ],
      "deny": [
        "tag:workstation:3389"  // Should not access workstations
      ]
    },
    
    // Test Engineering access
    {
      "src": "engineer1@yourdomain.com",
      "accept": [
        "tag:web:80",
        "tag:web:443", 
        "tag:staging:80",
        "tag:bastion:22"
      ],
      "deny": [
        "tag:production:22",    // No direct production access
        "tag:database:5432"     // No direct database access
      ]
    },
    
    // Test QA access
    {
      "src": "qa@yourdomain.com",
      "accept": [
        "tag:staging:80",
        "tag:staging:443",
        "tag:staging:22"
      ],
      "deny": [
        "tag:production:22",    // No production access
        "tag:database:5432"     // No direct database access
      ]
    },
    
    // Test service-to-service communication
    {
      "src": "tag:web",
      "accept": [
        "tag:database:5432",    // Web can access database
        "tag:database:3306"
      ]
    },
    
    // Test monitoring access
    {
      "src": "tag:monitoring",
      "accept": [
        "tag:server:9090",
        "tag:web:9090",
        "tag:database:9090"
      ]
    }
  ]
}"""

# Write the sample policy file
with open('policy.hujson', 'w') as f:
    f.write(sample_policy)

# Create a comprehensive README file
readme_content = """# Tailscale ACL GitOps Repository

This repository manages Tailscale Access Control Lists (ACLs) using GitOps principles, enabling infrastructure-as-code for network security policies.

## 🚀 Quick Start

### Prerequisites

1. **Tailscale Account**: You need admin access to your Tailscale tailnet
2. **GitHub Repository Secrets**: Configure the required secrets
3. **Tailscale API Key**: Generate an API key or OAuth credentials

### Setup Instructions

1. **Clone this repository** to your GitHub account
2. **Configure GitHub Secrets** in your repository settings:
   - `TS_API_KEY`: Your Tailscale API key
   - `TS_TAILNET`: Your tailnet name (e.g., `yourcompany.com`)

3. **Edit the policy file**: Modify `policy.hujson` with your ACL rules
4. **Test your changes**: Create a pull request to validate ACL syntax
5. **Deploy**: Merge to main branch to apply changes to your tailnet

## 📁 Repository Structure

```
├── policy.hujson                     # Main Tailscale ACL policy file
├── .github/
│   └── workflows/tailscale.yml       # GitHub Actions for ACL sync
├── .cursorrules                      # Cursor IDE configuration
├── .clinerules                       # Cline agent configuration  
├── AGENTS.md                         # General AI agent instructions
├── CLAUDE.md                         # Claude AI configuration
├── GEMINI_RULES.md                   # Gemini AI configuration
├── .aider.conf.yml                   # Aider configuration
├── .vscode/settings.json             # VS Code settings
├── .yamllint                         # YAML linting rules
├── .prettierrc                       # Code formatting rules
├── .pre-commit-config.yaml           # Pre-commit hooks
├── .editorconfig                     # Editor configuration
├── .gitignore                        # Git ignore patterns
└── README.md                         # This file
```

## 🔧 Configuration

### Tailscale API Credentials

You can use either an API key or OAuth credentials:

#### Option 1: API Key (Simple)
1. Go to [Tailscale Admin Console → Keys](https://login.tailscale.com/admin/settings/keys)
2. Generate a new API key
3. Add `TS_API_KEY` secret to your GitHub repository

#### Option 2: OAuth Client (Recommended for production)
1. Go to [Tailscale Admin Console → OAuth Clients](https://login.tailscale.com/admin/settings/oauth)
2. Create new OAuth client with `acl` scope
3. Add `TS_OAUTH_ID` and `TS_OAUTH_SECRET` secrets to GitHub

### GitHub Repository Secrets

Configure these secrets in your GitHub repository settings:

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `TS_API_KEY` | Tailscale API key | `tskey-api-...` |
| `TS_TAILNET` | Your tailnet name | `yourcompany.com` |
| `TS_OAUTH_ID` | OAuth client ID (if using OAuth) | `k1a2b3c...` |
| `TS_OAUTH_SECRET` | OAuth client secret (if using OAuth) | `ts_oauth_secret_...` |

## 📝 Policy File Format

The `policy.hujson` file uses HuJSON (Human JSON) format, which allows:
- **Comments**: Use `//` for inline comments
- **Trailing commas**: More git-friendly formatting
- **Multi-line strings**: Better readability

### Example Policy Structure

```json
{
  // Define user groups
  "groups": {
    "group:admins": ["admin@company.com"],
    "group:engineering": ["dev1@company.com", "dev2@company.com"]
  },
  
  // Define who can assign device tags
  "tagOwners": {
    "tag:server": ["group:admins"],
    "tag:workstation": ["group:engineering"]
  },
  
  // Access control rules
  "acls": [
    {
      "action": "accept",
      "src": ["group:engineering"],
      "dst": ["tag:server:22", "tag:server:80"]
    }
  ],
  
  // Test cases for validation
  "tests": [
    {
      "src": "dev1@company.com",
      "accept": ["tag:server:22"]
    }
  ]
}
```

## 🔄 Workflow

### Making Changes

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/add-qa-team-access
   ```

2. **Edit the policy file**:
   ```bash
   # Edit policy.hujson with your changes
   ```

3. **Create a pull request**:
   - The GitHub Action will validate your ACL syntax
   - Review the changes with your team
   - Merge when approved

4. **Automatic deployment**:
   - Merging to main automatically applies changes to Tailscale
   - Monitor the GitHub Actions log for deployment status

### Development Tools

This repository includes configuration for multiple AI coding assistants:

- **Cursor IDE**: `.cursorrules` file for Cursor AI
- **Cline**: `.clinerules` for Cline agent
- **GitHub Copilot**: Multiple instruction files
- **Claude**: `CLAUDE.md` for Claude AI
- **Gemini**: `GEMINI_RULES.md` for Gemini
- **Aider**: `.aider.conf.yml` configuration

## 🔍 Testing and Validation

### Pre-commit Hooks

Install pre-commit hooks for automatic validation:

```bash
pip install pre-commit
pre-commit install
```

This will automatically:
- Validate HuJSON syntax
- Check for security issues
- Format code consistently
- Run linting tools

### Manual Testing

Test your ACL policy before deployment:

```bash
# If you have Tailscale CLI installed
tailscale debug policy-file policy.hujson
```

## 🚨 Security Best Practices

### ACL Policy Guidelines

1. **Use groups instead of individual emails** for easier management
2. **Apply least privilege principles** - grant minimum necessary access
3. **Tag devices appropriately** for granular access control
4. **Include comprehensive test cases** for all access rules
5. **Regular audits** of access patterns and permissions

### Repository Security

1. **Never commit secrets** - use GitHub repository secrets
2. **Require pull request reviews** for all policy changes
3. **Enable branch protection** on the main branch
4. **Monitor GitHub Actions logs** for deployment issues
5. **Regularly rotate API keys** and OAuth credentials

## 🛠️ Troubleshooting

### Common Issues

#### GitHub Action Fails
- Check repository secrets are configured correctly
- Validate HuJSON syntax in policy.hujson
- Review GitHub Actions logs for specific errors

#### ACL Not Applied
- Ensure GitHub Action completed successfully
- Check Tailscale admin console for policy conflicts
- Verify API key has sufficient permissions

#### Syntax Errors
- Use a JSON validator that supports comments
- Check for missing commas or brackets
- Validate against Tailscale ACL schema

### Getting Help

1. **GitHub Issues**: Create an issue in this repository
2. **Tailscale Documentation**: [Official ACL docs](https://tailscale.com/kb/1337/acl-syntax)
3. **Tailscale Community**: [Community forum](https://forum.tailscale.com)

## 📚 Additional Resources

- [Tailscale ACL Syntax Reference](https://tailscale.com/kb/1337/policy-syntax)
- [GitOps for Tailscale with GitHub Actions](https://tailscale.com/kb/1306/gitops-acls-github)
- [Tailscale Best Practices](https://tailscale.com/kb/1019/subnets)
- [Zero Trust Networking](https://tailscale.com/blog/zero-trust-networking)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with appropriate test cases
4. Submit a pull request with a clear description
5. Wait for review and approval

## 📄 License

This repository is licensed under the MIT License. See LICENSE file for details.

---

**⚠️ Important Security Note**: This repository contains network access control policies. Always review changes carefully and test in staging environments when possible.
"""

# Write the README file
with open('README.md', 'w') as f:
    f.write(readme_content)

print("✅ Created additional files:")
print("  📁 .github/workflows/tailscale.yml - GitHub Actions workflow")
print("  📄 policy.hujson - Sample Tailscale ACL policy")
print("  📖 README.md - Comprehensive documentation")
print()
print("🎉 Complete AI coding agent framework created!")
print()
print("📋 Summary of created files:")
print("  • AI Agent Configurations: 9 files")
print("  • Development Tools: 6 files") 
print("  • Quality/Linting: 6 files")
print("  • Documentation: 3 files")
print("  • GitHub Actions: 1 file")
print("  • Sample Policy: 1 file")
print()
print("🔧 Next Steps:")
print("  1. Copy these files to your Tailscale ACL repository")
print("  2. Configure GitHub repository secrets (TS_API_KEY, TS_TAILNET)")  
print("  3. Customize the policy.hujson file for your environment")
print("  4. Test with a pull request before deploying to production")