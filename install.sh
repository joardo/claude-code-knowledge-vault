#!/usr/bin/env bash
# ==============================================================================
# Claude Platform Master Skill - Universal Installer
# Compatible with Claude Code and Google Antigravity
# Works locally or via: curl -fsSL https://raw.githubusercontent.com/.../install.sh | bash
# ==============================================================================

set -euo pipefail

REPO_OWNER="joardo"
REPO_NAME="claude-code-knowledge-vault"
BRANCH="main"
RAW_BASE_URL="https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/${BRANCH}"

SKILL_NAME="claude-platform-master"
TARGET_ENV="auto"
TARGET_SCOPE="global"
DRY_RUN=false
UNINSTALL=false

# ANSI colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

print_banner() {
    echo -e "${BLUE}${BOLD}"
    echo "=========================================================="
    echo "  Claude Platform Master Skill Installer"
    echo "  Expert Tool Selection Architect for Claude Code"
    echo "=========================================================="
    echo -e "${NC}"
}

usage() {
    echo -e "${BOLD}Usage:${NC} $0 [options]"
    echo ""
    echo "Options:"
    echo "  --global          Install globally for all projects (default)"
    echo "  --project         Install locally into current workspace project"
    echo "  --claude          Target Claude Code specifically"
    echo "  --antigravity     Target Google Antigravity specifically"
    echo "  --dry-run         Simulate installation without making changes"
    echo "  --uninstall       Remove the skill from the target location"
    echo "  -h, --help        Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0                # Default global install (auto-detects environment)"
    echo "  $0 --project      # Install into current project repo"
    echo "  $0 --dry-run      # Check where it would install"
    exit 0
}

# Parse CLI arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --global) TARGET_SCOPE="global"; shift ;;
        --project) TARGET_SCOPE="project"; shift ;;
        --claude) TARGET_ENV="claude"; shift ;;
        --antigravity) TARGET_ENV="antigravity"; shift ;;
        --dry-run) DRY_RUN=true; shift ;;
        --uninstall) UNINSTALL=true; shift ;;
        -h|--help) usage ;;
        *) echo -e "${RED}Unknown option: $1${NC}"; usage ;;
    esac
done

# Resolve Environment & Target Directory
resolve_paths() {
    if [[ "$TARGET_ENV" == "auto" ]]; then
        if [[ -d "$HOME/.gemini" ]] && [[ ! -d "$HOME/.claude" ]]; then
            TARGET_ENV="antigravity"
        elif [[ -d "$HOME/.claude" ]] && [[ ! -d "$HOME/.gemini" ]]; then
            TARGET_ENV="claude"
        elif [[ -d "$HOME/.claude" ]] && [[ -d "$HOME/.gemini" ]]; then
            # Both exist - default to claude but notify
            TARGET_ENV="claude"
        else
            TARGET_ENV="claude"
        fi
    fi

    if [[ "$TARGET_ENV" == "claude" ]]; then
        if [[ "$TARGET_SCOPE" == "global" ]]; then
            DEST_DIR="$HOME/.claude/skills/${SKILL_NAME}"
        else
            DEST_DIR="./.claude/skills/${SKILL_NAME}"
        fi
    else
        # Antigravity
        if [[ "$TARGET_SCOPE" == "global" ]]; then
            DEST_DIR="$HOME/.gemini/config/skills/${SKILL_NAME}"
        else
            DEST_DIR="./.agents/skills/${SKILL_NAME}"
        fi
    fi
}

install_files() {
    local script_dir
    script_dir="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || echo "")"
    local local_skill_dir="${script_dir}/skills/${SKILL_NAME}"

    if $DRY_RUN; then
        echo -e "${YELLOW}[DRY-RUN] Target Environment : ${TARGET_ENV}${NC}"
        echo -e "${YELLOW}[DRY-RUN] Target Scope       : ${TARGET_SCOPE}${NC}"
        echo -e "${YELLOW}[DRY-RUN] Destination Path   : ${DEST_DIR}${NC}"
        echo -e "${GREEN}[DRY-RUN] Dry run complete. No files were written.${NC}"
        return 0
    fi

    if $UNINSTALL; then
        if [[ -d "$DEST_DIR" ]]; then
            rm -rf "$DEST_DIR"
            echo -e "${GREEN}Successfully removed skill from: ${DEST_DIR}${NC}"
        else
            echo -e "${YELLOW}Skill was not found at: ${DEST_DIR}${NC}"
        fi
        return 0
    fi

    echo -e "${BLUE}Target Environment : ${BOLD}${TARGET_ENV}${NC}"
    echo -e "${BLUE}Target Scope       : ${BOLD}${TARGET_SCOPE}${NC}"
    echo -e "${BLUE}Destination Path   : ${BOLD}${DEST_DIR}${NC}"
    echo ""

    mkdir -p "${DEST_DIR}/references"

    # Check if we are running from a local git clone
    if [[ -d "$local_skill_dir" ]] && [[ -f "${local_skill_dir}/SKILL.md" ]]; then
        echo -e "Installing from local source: ${local_skill_dir}..."
        cp -r "${local_skill_dir}/"* "${DEST_DIR}/"
    else
        echo -e "Installing via remote download from ${RAW_BASE_URL}..."
        curl -fsSL "${RAW_BASE_URL}/skills/${SKILL_NAME}/SKILL.md" -o "${DEST_DIR}/SKILL.md"
        curl -fsSL "${RAW_BASE_URL}/skills/${SKILL_NAME}/references/capability_cheat_sheet.md" -o "${DEST_DIR}/references/capability_cheat_sheet.md"
        curl -fsSL "${RAW_BASE_URL}/skills/${SKILL_NAME}/references/consultation_examples.md" -o "${DEST_DIR}/references/consultation_examples.md"
    fi

    echo -e "${GREEN}${BOLD}Installation Successful!${NC}"
    echo ""
    echo -e "Skill installed to: ${DEST_DIR}"
    echo ""
    echo -e "${BOLD}Next Steps:${NC}"
    if [[ "$TARGET_ENV" == "claude" ]]; then
        echo -e "  1. Open Claude Code: ${GREEN}claude${NC}"
        echo -e "  2. Run the skill directly: ${GREEN}/claude-platform-master${NC}"
        echo -e "  3. Or ask naturally: ${YELLOW}\"What is the best Claude execution mode for long refactors?\"${NC}"
    else
        echo -e "  1. Start Antigravity: ${GREEN}agy${NC} (or launch IDE)"
        echo -e "  2. The skill is now active and ready for consultative advice."
    fi
}

print_banner
resolve_paths
install_files
