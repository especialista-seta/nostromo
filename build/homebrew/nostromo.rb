# typed: false
# frozen_string_literal: true

# Homebrew formula for NOSTROMO
# 
# To install locally:
#   brew install --build-from-source ./nostromo.rb
#
# To submit to Homebrew:
#   1. Fork homebrew-core
#   2. Add this formula to Formula/n/nostromo.rb
#   3. Submit PR

class Nostromo < Formula
  include Language::Python::Virtualenv

  desc "MU-TH-UR 6000 AI Interface - An Aliens-themed CLI chatbot"
  homepage "https://github.com/yourusername/nostromo"
  url "https://github.com/yourusername/nostromo/releases/download/v0.1.0/nostromo-0.1.0.tar.gz"
  sha256 "TODO_UPDATE_SHA256_ON_RELEASE"
  license "MIT"

  # Bottle block will be added by Homebrew CI
  # bottle do
  #   sha256 cellar: :any_skip_relocation, arm64_sonoma: "..."
  #   sha256 cellar: :any_skip_relocation, ventura: "..."
  #   sha256 cellar: :any_skip_relocation, x86_64_linux: "..."
  # end

  depends_on "python@3.11"

  # Main package
  resource "nostromo-cli" do
    url "https://files.pythonhosted.org/packages/.../nostromo_cli-0.1.0.tar.gz"
    sha256 "TODO_UPDATE_SHA256"
  end

  # Dependencies will be auto-populated by brew audit
  # resource "textual" do
  #   url "https://files.pythonhosted.org/packages/.../textual-0.89.0.tar.gz"
  #   sha256 "..."
  # end

  def install
    virtualenv_install_with_resources
  end

  def post_install
    ohai "NOSTROMO installed successfully!"
    ohai "Run 'nostromo configure' to set up your API keys"
  end

  def caveats
    <<~EOS
      ╔══════════════════════════════════════════════════════════════╗
      ║  MU-TH-UR 6000 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ USCSS NOSTROMO ║
      ╚══════════════════════════════════════════════════════════════╝

      First-time setup:
        nostromo configure

      Launch the interface:
        nostromo

      For more information:
        nostromo --help
    EOS
  end

  test do
    assert_match "MU-TH-UR 6000", shell_output("#{bin}/nostromo version")
  end
end
