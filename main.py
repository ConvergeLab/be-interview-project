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
        extractor.extract_traces_between_pads("U1", "20", "R2", "1") - 3.73421
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
        extractor.extract_traces_between_pads("R35", "2", "Q6", "4") - 2.07941
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("R32", "2", "Q6", "4") - 4.96667
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "22", "R17", "1") - 10.15418
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "15", "C2", "1") - 5.95187
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "19", "R15", "1") - 9.65903
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "47", "C38", "2") - 38.54960
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "6", "C26", "1") - 4.84104
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "66", "C28", "2") - 29.57893
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("R85", "1", "U1", "65") - 36.95201
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("R73", "2", "C31", "2") - 48.54113
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("C50", "1", "C41", "1") - 31.42141
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("R85", "1", "D8", "2") - 46.99169
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "21", "C12", "2") - 42.09864
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U2", "2", "C9", "2") - 22.30308
    ) < 0.1

    assert abs(
        extractor.extract_traces_between_pads("U1", "5", "U2", "2") - 21.451572
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
        extractor.extract_traces_between_pads("U1", "62", "R29", "1") - 48.45444
    ) < 0.1
