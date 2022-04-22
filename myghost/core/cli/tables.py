from myghost.core.cli.badges import Badges


class Tables:
    badges = Badges()

    def print_table(self, name, headers, *args, **kwargs) -> None:
        extra_fill = kwargs.get("extra_fill", 4)
        header_separator = kwargs.get("header_separator", "-")

        if not all(map(lambda x: len(x) == len(headers), args)):
            return

        def custom_len(x):
            x = str(x)
            try:
                if '\033' in x:
                    return len(x) - 9 * x.count('\033') // 2
                return len(x)
            except TypeError:
                return 0

        fill = list()
        headers_line = '    '
        headers_separator_line = '    '
        for idx, header in enumerate(headers):
            column = [custom_len(arg[idx]) for arg in args]
            column.append(len(header))

            current_line_fill = max(column) + extra_fill
            fill.append(current_line_fill)
            headers_line = "".join((headers_line, "{header:<{fill}}".format(header=header, fill=current_line_fill)))
            headers_separator_line = "".join((
                headers_separator_line,
                "{:<{}}".format(header_separator * len(header), current_line_fill)
            ))

        self.badges.print_empty('\n' + name.split()[0].title() + name[len(name.split()[0]):] + ':')
        self.badges.print_empty()
        self.badges.print_empty(headers_line)
        self.badges.print_empty(headers_separator_line)
        for arg in args:
            content_line = "    "
            for idx, element in enumerate(arg):
                element = str(element)
                fill_line = fill[idx]

                if '\033' in element:
                    fill_line = fill[idx] + 9 * element.count('\033') // 2

                content_line = "".join((
                    content_line,
                    "{:<{}}".format(element, fill_line)
                ))
            self.badges.print_empty(content_line)
        self.badges.print_empty()
