from trace_extractor import PCBTraceExtractor


if __name__ == "__main__":
    extractor = PCBTraceExtractor()
    extractor.load_json_file("Vacuum_PCB_OBjects.json")

    assert abs(
        extractor.extract_traces_between_pads("U1", "11", "R66", "1") - 5.30688
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "61", "C43", "2") - 5.90118
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "20", "C3", "2") - 2.09999
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "20", "R2", "1") - 4.009
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "9", "D5", "2") - 9.97167
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("R76", "1", "U1", "37") - 40.3965
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "4", "R54", "2") - 26.30932
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("R35", "2", "Q6", "4") - 1.9921
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("R32", "2", "Q6", "4") - 4.8794
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "22", "R17", "1") - 10.1542
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "15", "C2", "1") - 5.95187
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "19", "R15", "1") - 9.64036
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "47", "C38", "2") - 38.5496
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "6", "C26", "1") - 4.84104
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("R2", "1", "C3", "2") - 1.90922
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "9", "C21", "2") - 3.7029
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("D8", "2", "D4", "2") - 1.9909
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "62", "C44", "1") - 3.75556
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "62", "R29", "1") - 48.4302
    ) < 0.1

    assert extractor.extract_traces_between_pads("U1", "66", "C28", "2") is None

    assert extractor.extract_traces_between_pads("U1", "65", "R85", "1") is None

    assert extractor.extract_traces_between_pads("D8", "2", "R85", "1") is None

    assert extractor.extract_traces_between_pads("U2", "2", "C9", "2") is None

    assert extractor.extract_traces_between_pads("U1", "51", "R26", "2") is None

    assert extractor.extract_traces_between_pads("D5", "1", "R37", "2") is None
