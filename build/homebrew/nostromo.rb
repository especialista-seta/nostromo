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
  homepage "https://github.com/especialista-seta/nostromo"
  url "https://files.pythonhosted.org/packages/source/n/nostromo-cli/nostromo_cli-0.1.0.tar.gz"
  sha256 "9fbbfc6c7a84c750bf638067b805c8d4b9d824083ae2d6fec132c63a097c6c3a"
  license "MIT"

  depends_on "python@3.11"

  resource "nostromo-core" do
    url "https://files.pythonhosted.org/packages/source/n/nostromo-core/nostromo_core-0.1.0.tar.gz"
    sha256 "0b7c1958cfa5bcfb469adf4edd76eb0aa6859d9dd9633cb6de76502e2e503d2a"
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
