import argparse

from tools_system import ToolsSystem


def main():
    parser = argparse.ArgumentParser(description='Process Linux LLM tools args.')
    parser.add_argument('mode', type=str, help='system mode for Linux LLM tools: sys for system mode, program mode '
                                               'for once program')

    args = parser.parse_args()

    tools_system = ToolsSystem(args.mode)
    tools_system.run()


if __name__ == "__main__":
    main()