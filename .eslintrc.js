module.exports = {
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
};