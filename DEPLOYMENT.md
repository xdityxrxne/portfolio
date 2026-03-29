# 🚀 Deployment Guide

## Step 1: Push to GitHub

```bash
# Initialize git
git init
git add .
git commit -m "Initial commit: AI Engineer portfolio"

# Create a new repo on GitHub:
# Go to: https://github.com/new
# Repository name: portfolio
# Keep it PUBLIC
# Don't initialize with README
# Click "Create repository"

# Push to GitHub
git remote add origin https://github.com/xdityxrxne/portfolio.git
git branch -M main
git push -u origin main
```

## Step 2: Deploy to Vercel

### Option A: Vercel CLI (Fastest)
```bash
# Install Vercel CLI globally
npm install -g vercel

# Deploy (run from workspace root)
vercel

# Follow prompts:
# - Login with GitHub
# - Link to existing project? No
# - Project name: portfolio
# - Directory: ./ (current directory)
# - Override settings? No

# Your site will be live at: https://portfolio-<random>.vercel.app
```

### Option B: Vercel Web UI (Easier)
1. Go to: https://vercel.com/new
2. Click "Import Git Repository"
3. Authorize GitHub access
4. Select repository: `xdityxrxne/portfolio`
5. Click "Deploy"
6. Wait 30 seconds — done!

Your site will be live at: `https://portfolio-<random>.vercel.app`

## Step 3: Custom Domain (Optional)
1. Go to your Vercel project settings
2. Click "Domains"
3. Add your custom domain (e.g., adityarane.dev)
4. Follow DNS configuration instructions

---

## 🔧 Update Content Later

To update your portfolio:
1. Edit `index.html` locally
2. Commit and push:
   ```bash
   git add .
   git commit -m "Update projects"
   git push
   ```
3. Vercel auto-deploys on every push (takes ~30 seconds)

---

## 📝 Notes
- The site is 100% static HTML — no build step needed
- Vercel serves it instantly with global CDN
- All assets are in the repo (no external dependencies)
- Contact form uses mailto (no backend required)
